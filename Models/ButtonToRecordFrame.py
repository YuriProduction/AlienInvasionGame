import pygame


class RecordButton():
    def __init__(self):
        window_width = 1200
        button_font = pygame.font.SysFont("Arial", 15)
        self.button_text = button_font.render("Таблица рекордов", True, (0, 0, 0))
        button_width = self.button_text.get_width()
        button_height = self.button_text.get_height()
        self.button_x = window_width - button_width - 20
        self.button_y = 100
        self.rect = pygame.Rect(self.button_x, self.button_y, button_width, button_height)

    def draw(self, screen):
        screen.blit(self.button_text, (self.button_x, self.button_y))
