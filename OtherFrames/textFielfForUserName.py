import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_BACKSPACE


def get_name() -> str:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Name Input")

    font = pygame.font.Font(None, 32)

    label_text = "Enter your name:"
    label = font.render(label_text, True, BLACK)

    input_rect = pygame.Rect(240, 50, 150, 32)
    input_text = ""

    button_rect = pygame.Rect(200, 100, 50, 32)
    button_text = font.render("OK", True, BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:

                    input_text = input_text[:-1]
                else:

                    input_text += event.unicode
            elif event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    running = False

        if not running:
            break

        screen.fill(WHITE)

        screen.blit(label, (50, 50))

        pygame.draw.rect(screen, BLACK, input_rect, 2)
        input_surface = font.render(input_text, True, BLACK)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.draw.rect(screen, BLACK, button_rect, 2)
        screen.blit(button_text, (button_rect.x + 5, button_rect.y + 5))

        pygame.display.flip()
    screen = pygame.display.set_mode((1200, 800))
    return input_text
