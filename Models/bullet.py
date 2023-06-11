import pygame
from settings import Settings
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.settings = Settings()
        self.screen = screen
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.screen.get_rect().midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    # pragma: no cover
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
