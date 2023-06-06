import pygame, os
from pygame.sprite import Sprite, Group


class Bunker(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        try:
            image_path = os.path.join("Images", "Bunker_.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
        except FileNotFoundError:
            self.image = pygame.Surface((50, 50))  # Adjust the size of the bunker
            self.image.fill((255, 0, 0))  # Set the color to red
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 3

    def update(self):
        if self.health <= 0:
            self.kill()

    def hit(self):
        self.health -= 1

    # pragma: no cover
    def draw(self):
        self.screen.blit(self.image, self.rect)
