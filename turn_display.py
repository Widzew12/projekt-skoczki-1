import pygame

from static_variables import *


class TurnDisplay:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.white_pawn_image = pygame.image.load('images/white_pawn.bmp')
        self.black_pawn_image = pygame.image.load('images/black_pawn.bmp')

        self.image = self.white_pawn_image

        self.rect = self.image.get_rect()
        self.rect.topright = self.screen_rect.topright

        self.update_turn_display()

    def update_turn_display(self):
        if self.game.current_turn == WHITE:
            self.image = self.white_pawn_image
        elif self.game.current_turn == BLACK:
            self.image = self.black_pawn_image

    def update_screen(self):
        self.screen.blit(self.image, self.rect)
