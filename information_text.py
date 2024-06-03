import pygame.font


class InformationText:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.image_top = None
        self.rect_top = None

        self.image_bottom = None
        self.rect_bottom = None
        self.show_bottom_image = False

        self._init_end_move_text()

        self.change_top_text("")

    def change_top_text(self, msg):
        self.image_top = self.font.render(msg, True, self.text_color)
        self.rect_top = self.image_top.get_rect()
        self.rect_top.midtop = self.screen_rect.midtop
        self.rect_top.y += 10

    def _init_end_move_text(self):
        self.image_bottom = self.font.render("Press RETURN to end move", True, self.text_color)
        self.rect_bottom = self.image_bottom.get_rect()
        self.rect_bottom.midbottom = self.screen_rect.midbottom
        self.rect_bottom.y -= 10

    def show_end_move_text(self, show):
        self.show_bottom_image = show

    def update_screen(self):
        self.screen.blit(self.image_top, self.rect_top)
        if self.show_bottom_image:
            self.screen.blit(self.image_bottom, self.rect_bottom)
