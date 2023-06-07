import pygame, random, os
from settings import Settings


class Mystery_Ship(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        try:
            self.image = pygame.image.load(os.path.join('Images', 'Oh_hi_mark.webp'))
            self.rect = self.image.get_rect()
        except FileNotFoundError:
            self.image = pygame.Surface((50, 50))  # Adjust the size of the bunker
            self.image.fill((255, 0, 0))  # Set the color to red
            self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = random.randint(0, self.rect.height)
        self.speed = 1.7

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed / 2
        # pragma: no cover
        if self.rect.right < 0:
            self.rect.x = self.settings.screen_width
            self.rect.y = random.randint(0, self.settings.screen_height - self.rect.height)
