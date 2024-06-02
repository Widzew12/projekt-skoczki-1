import pygame

from static_variables import *

from game_board import GameBoard
from field import Field
from move import Move
from pawn import Pawn
from field_collider import FieldCollider


class FieldColliders:
    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings
        self.field_colliders = pygame.sprite.Group()
        self._initialize_board()

    def _initialize_board(self):
        new_field_pos_x = self.settings.first_field_pos_x
        new_field_pos_y = self.settings.first_field_pos_y

        for row_index in range(len(self.game.game_board.current_game_board_tuple)):
            for column_index in range(len(self.game.game_board.current_game_board_tuple[row_index])):
                field = Field(row_index, column_index, self.game.game_board.current_game_board_tuple)
                self.field_colliders.add(FieldCollider(self.game, (new_field_pos_x, new_field_pos_y), field))
                new_field_pos_x += self.settings.field_width
            new_field_pos_x = self.settings.first_field_pos_x
            new_field_pos_y += self.settings.field_height

        self.update_board()

    def update_board(self):
        self.field_colliders.update()
