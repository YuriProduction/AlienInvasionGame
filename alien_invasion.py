import sys
import threading
from time import sleep

import pygame

import Models.ButtonToRecordFrame as recordsButton
import OtherFrames.RecordFrame
import OtherFrames.textFielfForUserName
import Serializeble.loader
import Serializeble.saver
from Models.Pause import PauseButton
from Models.alien import Alien
from Models.bullet import Bullet
from Models.button import Button
from Models.ship import Ship
from game_stats import GameStats
from settings import Settings
from table import Table

pygame.mixer.init()
pygame.mixer.set_num_channels(Settings().sound_channels)
pygame.init()
back_music = pygame.mixer.Sound('Music/Game.wav')
back_music.set_volume(0.15)


class AlienInvasion:
    def _initialize_Settings_And_Screen(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.screen_rect = self.screen.get_rect()

    def _initialize_models(self):
        self.ship = Ship(self.screen)
        self.ship_height = 48

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.play_button = Button("Play", 200, 50)
        self.play_button.screen = self.screen
        self.play_button.draw_button()

        self.pause_button = PauseButton()
        self.records_button = recordsButton.RecordButton()

    def _initialize_statistics_and_Table(self):
        self.stats = GameStats()
        self.stats.game_active = False
        self.records = []
        self.number = 0
        self.table = Table(str(self.number))
        self.table.screen = self.screen

    def __init__(self):
        self._initialize_Settings_And_Screen()

        self._initialize_models()

        self._initialize_statistics_and_Table()

    def _ship_hit(self):
        if self.stats.ships_count > 0:
            self.stats.ships_count -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.rect.midbottom = self.screen_rect.midbottom
            self.ship.x = float(self.ship.rect.x)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit(1)
        elif event.key == pygame.K_SPACE:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Music/SHOOT.wav'))
            self._fire_bullet()

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_pause_button(self, mouse_pos):
        if self.pause_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = False

    def _check_records_button(self, mouse_pos):
        if self.records_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = False
            self._showTheScreenOfRecords()

    def _showTheScreenOfRecords(self):
        OtherFrames.RecordFrame.show_record_table(self.screen, self.records)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        self.settings.fleet_drop_speed += 5
        self.settings.alien_speed += 1.0
        self.settings.bullet_speed += 0.5
        alien = Alien()
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_of_aliens = avaliable_space_x // (2 * alien_width)

        avaliable_space_y = self.settings.screen_height - self.ship_height - 3 * alien_height
        number_rows = avaliable_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(numbers_of_aliens):
                self._create_alion(alien_number, row_number)

    def _create_alion(self, alien_number, number_rows):
        alien = Alien()
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * number_rows
        self.aliens.add(alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.screen)
            new_bullet.rect.midtop = self.ship.rect.midtop
            new_bullet.y = new_bullet.rect.y
            self.bullets.add(new_bullet)

    def _check_events(self, username):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.number != 0:
                    Serializeble.saver.save_data(self.number, username)
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_pause_button(mouse_pos)
                self._check_records_button(mouse_pos)

    def _update_records(self):
        self.records = sorted(Serializeble.loader.load_data(), key=lambda x: x[1], reverse=True)
        print(self.records)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.pause_button.draw(self.screen)
        self.records_button.draw(self.screen)
        if self.stats.game_active != True:
            self.play_button.draw_button()
            if self.stats.ships_count == 0:
                back_music.stop()
                ai = AlienInvasion()
                ai.run_game()

        else:
            self.table.draw_button(str(self.number))
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_alien_and_bullet_collision()

    def _check_alien_and_bullet_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True,
                                                True)
        if collisions:
            self.number += 1
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges(self.screen):
                self._change_fleet_directory()
                break

    def _change_fleet_directory(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= (-1)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update(self.settings.fleet_direction)
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def run_game(self):
        user_name = OtherFrames.textFielfForUserName.get_name()
        pygame.mixer.Channel(0).play(back_music)

        self._update_records()
        while True:
            self._check_events(user_name)
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
