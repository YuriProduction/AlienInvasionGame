import pygame


class PauseButton():
    def __init__(self):
        self.rect = pygame.Rect(10, 10, 30, 40)

    def draw(self, screen):
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        # создаем кнопку
        pausebutton = pygame.Rect(10, 10, 30, 40)
        pygame.draw.rect(screen, GREEN, pausebutton)
        pygame.draw.line(screen, WHITE, (20, 20), (20, 40), 5)
        pygame.draw.line(screen, WHITE, (30, 20), (30, 40), 5)
