import pygame
from pygame.sprite import Sprite

from static_variables import *


class Pawn(Sprite):
    def __init__(self, game, color, position):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        if color == WHITE:
            self.image = pygame.image.load('images/white_pawn.bmp')
        elif color == BLACK:
            self.image = pygame.image.load('images/black_pawn.bmp')

        self.rect = self.image.get_rect()

        self.rect.topleft = position

    def update(self):
        self.screen.blit(self.image, self.rect)
