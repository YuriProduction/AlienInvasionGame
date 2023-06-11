import unittest
import pygame
import os
from Models.bunker import Bunker


class TestBunker(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bunker = Bunker(self.screen, 100, 100)

    def test_init(self):
        self.assertEqual(self.bunker.health, 3)
        self.assertEqual(self.bunker.rect.x, 100)
        self.assertEqual(self.bunker.rect.y, 100)
        self.assertIsInstance(self.bunker.image, pygame.Surface)

    def test_update(self):
        self.bunker.health = 0
        self.bunker.update()
        self.assertFalse(self.bunker.alive())

    def test_hit(self):
        initial_health = self.bunker.health
        self.bunker.hit()
        self.assertEqual(self.bunker.health, initial_health - 1)

    def tearDown(self):
        pygame.quit()
