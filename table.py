import pygame as pg
from settings import Settings


# pragma : no cover
class Table:
    def __init__(self, msg):
        self.settings = Settings()
        self.screen = pg.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = self.settings.table_width, self.settings.table_height
        self.button_color = self.settings.table_button_color
        self.text_color = self.settings.table_text_color
        self.font = pg.font.SysFont(None, self.settings.table_font_size)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        self.draw_button(msg)

    def draw_button(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
