import os, pygame, sys
import time
from time import sleep
from settings import Settings
from alien import Alien
from ship import Ship
from bullet import Bullet
from button import Button
from table import Table
from game_stats import GameStats

pygame.mixer.init()
pygame.mixer.set_num_channels(Settings().sound_channels)


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.screen_rect = self.screen.get_rect()
        # Statistic
        self.stats = GameStats()
        self.stats.game_active = False
        # Ship
        self.ship = Ship()
        self.ship.screen = self.screen  # Two dofferent screens
        self.ship_height = 48

        # Bullets
        self.bullets = pygame.sprite.Group()  # типо списка в пайгейм, Group - это класс

        # Alien
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Button
        self.play_button = Button("Play")
        self.play_button.screen = self.screen
        self.play_button.draw_button()

        # Table
        self.number = 0
        self.table = Table(str(self.number))
        self.table.screen = self.screen
        # .draw_button()
        # self.table.change_numbers_and_draw_table(self.number)

    def _ship_hit(self):
        if self.stats.ships_count > 0:
            self.stats.ships_count -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.rect.midbottom = self.screen_rect.midbottom
            self.ship.x = float(self.ship.rect.x)

            sleep(0.5)
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
            self._fire_bullet()

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keyup_events(self, event):
        # если отжали кнопку, то больше не двигаемся
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
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
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Music/shoot.wav'))
        #  если пулек не больше, чем мы установили в настройках, то все ок!
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet()
            new_bullet.screen = self.screen
            # выравниваем пульку относительно корабля
            new_bullet.rect.midtop = self.ship.rect.midtop
            new_bullet.y = new_bullet.rect.y
            self.bullets.add(new_bullet)

    def _check_events(self):
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if self.stats.game_active != True:
            self.play_button.draw_button()
        else:
            self.table.draw_button(str(self.number))
        pygame.display.flip()  # отображение последнего прорисованного экрана

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_alien_and_bullet_collision()

    def _check_alien_and_bullet_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True,
                                                True)  # False,True - не удаляем снаряды, но удаляем НЛО
        if collisions:
            self.number += 1
        if not self.aliens:  # new fleet if we have killed every ship
            self.bullets.empty()
            self._create_fleet()
        # self.number+=1

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
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Music/Game.wav'))
        while True:
            self._check_events()
            if self.stats.game_active:
                # во время игры
                # постоянно обновляем расположения
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            # else:
            #     pygame.mixer.music.pause()
            self._update_screen()


if __name__ == '__main__':  # __name__ хранит в контексте какого файла он запускается, __main__ соответсвует текцщему файлу
    ai = AlienInvasion()
    ai.run_game()
