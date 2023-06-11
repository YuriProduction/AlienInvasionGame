import unittest

import pygame

from Models.bullet import Bullet


class TestBullet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bullet = Bullet(self.screen)

    def test_init(self):
        self.assertEqual(self.bullet.settings.bullet_color, (60, 60, 60))
        self.assertEqual(self.bullet.rect.width, 3)
        self.assertEqual(self.bullet.rect.height, 15)

    def test_update(self):
        y = self.bullet.y
        self.bullet.update()
        self.assertEqual(self.bullet.y, y - self.bullet.settings.bullet_speed)

    def tearDown(self):
        pygame.quit()
