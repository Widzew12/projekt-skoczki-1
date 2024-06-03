import pygame

from static_variables import *


class GameEndDisplay:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        self.white_won_image = pygame.image.load('images/white_won_image.bmp')
        self.black_won_image = pygame.image.load('images/black_won_image.bmp')

        self.image = None
        self.rect = None

    def init_game_end_display(self):
        if self.game.win == WHITE:
            self.image = self.white_won_image
        elif self.game.win == BLACK:
            self.image = self.black_won_image

        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def update_screen(self):
        self.screen.blit(self.image, self.rect)
