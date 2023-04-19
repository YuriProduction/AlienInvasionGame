import pygame as pg
import pygame.font


class Button:
    def __init__(self, msg):
        self.screen = pg.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()

        # features of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        # button as rect object
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg = "Play"
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)