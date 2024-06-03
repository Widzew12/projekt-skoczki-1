from game_board import GameBoard
from static_variables import *

from field import Field


class Move:
    def __init__(self, starting_field: Field, target_field: Field, game_board: GameBoard):
        """Initialize the move class with starting and target fields."""
        self.starting_field = starting_field
        self.target_field = target_field
        self.middle_field = None
        self.board = game_board
        self.new_board_tuple = game_board.current_game_board_tuple
        self.long_move_performed = False

    def check_and_make_next_move(self, previous_move):
        if not previous_move.target_field.index == self.starting_field.index:
            return False

        if previous_move.starting_field.index == self.target_field.index:
            return False

        if not self._check_starting_and_target_field():
            return False

        elif self._try_make_long_move():
            return True
        return False

    def check_and_make_move(self):
        """Checks if the move is valid and performs it; the result is saved in new_board_tuple."""
        if not self._check_starting_and_target_field():
            return False

        # Check if move is by 1 or more fields
        if self._try_make_short_move():
            return True

        elif self._try_make_long_move():
            return True
        return False

    def _check_starting_and_target_field(self):
        """Checks if starting and target fields are not the same fields and if target field is empty"""
        # Check if starting field is not the same as target field
        # Also check if target field is not empty
        if self.starting_field.index == self.target_field.index or self.target_field.content != EMPTY:
            return False
        return True

    def _check_for_short_move(self):
        """Check if a short move is valid."""
        return ((self.starting_field.row_index == self.target_field.row_index - 1 or
                 self.starting_field.row_index == self.target_field.row_index + 1) and
                (self.starting_field.column_index == self.target_field.column_index - 1 or
                 self.starting_field.column_index == self.target_field.column_index + 1))

    def _check_for_long_move(self):
        """Check if a long move is valid"""
        return ((self.starting_field.row_index == self.target_field.row_index + 2 or
                 self.starting_field.row_index == self.target_field.row_index - 2) and
                (self.starting_field.column_index == self.target_field.column_index + 2 or
                 self.starting_field.column_index == self.target_field.column_index - 2))

    def _try_make_short_move(self):
        # Check if move is by 1 or more fields
        if self._check_for_short_move():
            self._make_move()
            return True
        return False

    def _try_make_long_move(self):
        # Check if move is performed by 2 fields and if it is performed diagonally.
        # Also check if a middle field exists and has content - only then you can make a long move
        if self._check_for_long_move() and self._find_and_check_middle_field():
            self._make_move()
            self.long_move_performed = True
            return True
        return False

    def _make_move(self):
        """Make a move; check if the move is valid before using this method!"""
        self.new_board_tuple[self.target_field.row_index][self.target_field.column_index] = self.starting_field.content
        self.new_board_tuple[self.starting_field.row_index][self.starting_field.column_index] = EMPTY

    def _find_and_check_middle_field(self):
        """Checks if a middle field exists and if it isn't empty."""
        # Calculate middle field index
        middle_field_row_index = (self.starting_field.row_index + self.target_field.row_index) / 2
        middle_field_column_index = (self.starting_field.column_index + self.target_field.column_index) / 2

        # Check if the middle field index is an integer - if it isn't, then the middle field doesn't exist.
        if not (middle_field_row_index.is_integer() and middle_field_column_index.is_integer()):
            return False

        # Create a middle_field Field object.
        self.middle_field = Field(int(middle_field_row_index), int(middle_field_column_index),
                                  self.board.current_game_board_tuple)

        # Check if the middle field has content - if it doesn't, you can't make a long move.
        if self.middle_field.content == EMPTY:
            return False

        # If all the requirements are met, return True - the middle field exists and has content.
        return True
