import pygame

from static_variables import *

from game_board import GameBoard
from field import Field
from move import Move
from pawn import Pawn


class GameBoardDisplay:
    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings
        self.pawns = pygame.sprite.Group()
        self.change_board()

    def change_board(self):
        new_pawn_pos_x = self.settings.first_field_pos_x
        new_pawn_pos_y = self.settings.first_field_pos_y
        for row in self.game.game_board.current_game_board_tuple:
            for field_content in row:
                if field_content == EMPTY:
                    pass
                else:
                    self.pawns.add(Pawn(self.game, field_content, (new_pawn_pos_x, new_pawn_pos_y)))
                new_pawn_pos_x += self.settings.field_width
            new_pawn_pos_x = self.settings.first_field_pos_x
            new_pawn_pos_y += self.settings.field_height
        self.update_board()

    def update_board(self):
        self.pawns.update()
