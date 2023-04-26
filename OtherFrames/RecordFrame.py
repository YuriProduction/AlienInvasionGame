import pygame


def show_record_table(scores: list):
    # Определение цветов
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Инициализация Pygame
    pygame.init()

    # Создание окна
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Таблица рекордов")

    # Шрифты
    font_small = pygame.font.SysFont('Arial', 20)
    font_large = pygame.font.SysFont('Arial', 40)

    # Основной цикл программы
    done = False
    while not done:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        # Очистка экрана
        screen.fill(WHITE)

        # Заголовок
        title_text = font_large.render("Таблица рекордов", True, BLACK)
        title_rect = title_text.get_rect()
        title_rect.center = (size[0] // 2, 50)
        screen.blit(title_text, title_rect)

        # Таблица рекордов
        y = 100
        for i, (name, score) in enumerate(scores):
            name_text = font_small.render(name, True, BLACK)
            name_rect = name_text.get_rect()
            name_rect.left = 50
            name_rect.top = y
            screen.blit(name_text, name_rect)

            score_text = font_small.render(str(score), True, BLACK)
            score_rect = score_text.get_rect()
            score_rect.right = size[0] - 50
            score_rect.top = y
            screen.blit(score_text, score_rect)

            y += 30

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()
