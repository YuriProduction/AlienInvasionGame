import pygame, os, random
from settings import Settings
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.speed_of_aliens = self.settings.alien_speed

        try:
            image_path = os.path.join("Images", "NLO.png")
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()

            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
        except FileNotFoundError:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)

    def check_edges(self, screen):
        screen_rect = screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, fleet_direction):
        self.x += (self.speed_of_aliens * fleet_direction)
        self.rect.x = self.x
