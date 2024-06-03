import pygame.font


class InformationText:
    def __init__(self, game):
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
        self.rect.midtop = self.screen_rect.midtop
        print(f"width: {self.rect.width}")
        print(f"height: {self.rect.height}")

    def update_screen(self):
        self.screen.blit(self.image, self.rect)
