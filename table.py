import pygame as pg
import pygame.font


class Table:
    def __init__(self, msg):
        self.screen = pg.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()

        # features of button
        self.width, self.height = 100, 50
        self.button_color = (233, 233, 233)
        self.text_color = (0, 0, 0)
        self.font = pg.font.SysFont(None, 48)

        # button as rect object
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        # self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        # self.msg_image_rect = self.msg_image.get_rect()
        # self.msg_image_rect.center = self.rect.center
        self.draw_button(msg)

    def draw_button(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
