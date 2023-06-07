import pygame
from settings import Settings


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def initialize(self, screen):
        pygame.init()
        self.settings = Settings()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        try:
            self.image = pygame.image.load('Images/ship.bmp')
            self.rect = self.image.get_rect()
        except FileNotFoundError:
            self.image = pygame.Surface((50, 50))  # Adjust the size of the bunker
            self.image.fill((255, 0, 0))  # Set the color to red
            self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
