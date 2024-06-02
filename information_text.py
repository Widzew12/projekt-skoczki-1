import pygame.font
from pygame.sprite import Sprite


class InformationText(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 72)

        self.image = None
        self.rect = None

        self.change_text("")

    def change_text(self, msg):
        self.image = self.font.render(msg, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.update_screen()
        print(f"width: {self.rect.width}")
        print(f"height: {self.rect.height}")

    def update_screen(self):
        self.image.blit(self.image, self.rect)
