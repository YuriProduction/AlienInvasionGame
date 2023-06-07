
from unittest import TestCase
import pygame
from settings import Settings
from Models.alien import Alien


class TestAlien(TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.alien = Alien()

    def test_init(self):
        self.assertIsInstance(self.alien.settings, Settings)
        self.assertIsInstance(self.alien.screen, pygame.Surface)
        self.assertEqual(self.alien.speed_of_aliens, self.alien.settings.alien_speed)
        self.assertIsInstance(self.alien.image, pygame.Surface)
        self.assertIsInstance(self.alien.rect, pygame.Rect)
        self.assertEqual(self.alien.rect.x, self.alien.rect.width)
        self.assertEqual(self.alien.rect.y, self.alien.rect.height)
        self.assertIsInstance(self.alien.x, float)

    def test_check_edges(self):
        self.screen_rect = self.screen.get_rect()
        self.alien.rect.right = self.screen_rect.right + 1
        self.assertTrue(self.alien.check_edges(self.screen))
        self.alien.rect.right = self.screen_rect.right - 1
        self.assertFalse(self.alien.check_edges(self.screen))
        self.alien.rect.left = -1
        self.assertTrue(self.alien.check_edges(self.screen))
        self.alien.rect.left = 0
        self.assertTrue(self.alien.check_edges(self.screen))

    def test_update(self):
        fleet_direction = 1
        old_x = self.alien.x
        self.alien.update(fleet_direction)
        new_x = self.alien.x
        self.assertEqual(new_x, old_x + (self.alien.speed_of_aliens * fleet_direction))

    def tearDown(self):
        pygame.quit()

