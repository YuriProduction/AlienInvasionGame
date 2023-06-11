import unittest
import pygame
from Models.mystery_ship import Mystery_Ship
from settings import Settings


class TestMysteryShip(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.mystery_ship = Mystery_Ship()

    def test_sprite_created(self):
        self.assertIsInstance(self.mystery_ship, pygame.sprite.Sprite)

    def test_image_loaded(self):
        self.assertIsNotNone(self.mystery_ship.image)

    def test_speed_set(self):
        self.assertEqual(self.mystery_ship.speed, 1.7)

    def test_random_y_coordinate(self):
        self.assertGreaterEqual(self.mystery_ship.rect.y, 0)
        self.assertLessEqual(self.mystery_ship.rect.y, 600)

    def test_ship_moves_right(self):
        initial_x = self.mystery_ship.rect.x
        self.mystery_ship.update()
        self.assertGreater(self.mystery_ship.rect.x, initial_x)

    def tearDown(self):
        pygame.quit()
