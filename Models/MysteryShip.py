import pygame, random
from settings import Settings
from Models.alien import Alien


class MysteryShip(Alien):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/Oh_hi_mark.webp')
