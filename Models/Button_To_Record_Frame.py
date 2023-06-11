import pygame

from settings import Settings


# pragma: no cover
class RecordButton():
    # pragma: no cover
    def __init__(self):
        self.settings = Settings()
        button_font = pygame.font.SysFont("Arial", self.settings.font_size)
        self.button_text = button_font.render("Таблица рекордов", True, (0, 0, 0))
        button_width = self.button_text.get_width()
        button_height = self.button_text.get_height()
        print(button_height, button_width)
        self.button_x = self.settings.layoutX
        self.button_y = self.settings.layoutY  # self.settings.screen_height
        self.rect = pygame.Rect(self.button_x, self.button_y, button_width, button_height)

    # pragma: no cover
    def draw(self, screen):
        screen.blit(self.button_text, (self.button_x, self.button_y))
