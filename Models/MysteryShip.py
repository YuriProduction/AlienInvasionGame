import pygame, random
from settings import Settings


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.image = pygame.image.load('Images/Oh_hi_mark.webp')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = self.settings.fleet_drop_speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.settings.screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)

    def check_edges(self, screen):
        screen_rect = screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
