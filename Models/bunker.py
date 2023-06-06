import pygame, os
from pygame.sprite import Sprite, Group


class Bunker(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        image_path = os.path.join("Images", "Bunker_.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 3

    def update(self):
        if self.health <= 0:
            self.kill()

    def hit(self):
        self.health -= 1

    def draw(self):
        self.screen.blit(self.image, self.rect)

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen_width = 800
#         self.screen_height = 600
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Alien Invasion")
#         self.clock = pygame.time.Clock()
#         self.BLACK = (0, 0, 0)
#         self.bunkers = Group()
#         self.create_bunkers()
#
#     def create_bunkers(self):
#         bunker_spacing = 200
#         num_bunkers = 3
#         bunker_start_x = (self.screen_width - (num_bunkers * bunker_spacing)) // 2
#         bunker_y = self.screen_height - 150
#
#         for i in range(num_bunkers):
#             bunker_x = bunker_start_x + (i * bunker_spacing)
#             bunker = Bunker(self.screen, bunker_x, bunker_y)
#             self.bunkers.add(bunker)
#
#     def run(self):
#         while True:
#             self.handle_events()
#             self.update()
#             self.draw()
#             self.clock.tick(60)
#
#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#
#     def update(self):
#         self.bunkers.update()
#
#     def draw(self):
#         self.screen.fill(self.BLACK)
#         self.bunkers.draw(self.screen)
#         pygame.display.flip()
#
# if __name__ == '__main__':
#     game = Game()
#     game.run()
