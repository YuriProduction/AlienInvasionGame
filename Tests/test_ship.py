import unittest
import pygame
from Models.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.ship = Ship()
        self.ship.initialize(self.screen)

    def test_sprite_created(self):
        self.assertIsInstance(self.ship, pygame.sprite.Sprite)

    def test_image_loaded(self):
        self.assertIsNotNone(self.ship.image)

    def test_initialize_screen(self):
        self.assertEqual(self.ship.screen, self.screen)

    def test_initialize_settings(self):
        self.assertIsNotNone(self.ship.settings)

    def test_ship_starts_at_bottom_center(self):
        self.assertEqual(self.ship.rect.midbottom, self.screen.get_rect().midbottom)

    def test_ship_moves_right(self):
        initial_x = self.ship.rect.x
        self.ship.moving_right = True
        self.ship.update()
        self.assertGreater(self.ship.rect.x, initial_x)

    def test_ship_moves_left(self):
        initial_x = self.ship.rect.x
        self.ship.moving_left = True
        self.ship.update()
        self.assertLess(self.ship.rect.x, initial_x)

    def test_ship_stops_at_left_edge(self):
        self.ship.moving_left = True
        self.ship.rect.x = 0
        self.ship.update()
        self.assertEqual(self.ship.rect.x, 0)

    def test_ship_stops_at_right_edge(self):
        self.ship.moving_right = True
        self.ship.rect.right = self.screen.get_rect().right
        self.ship.update()
        self.assertEqual(self.ship.rect.right, self.screen.get_rect().right)

    def tearDown(self):
        pygame.quit()
