from static_variables import STARTING_BOARD


class GameBoard:
    """A class that stores the game board and data related to it."""

    def __init__(self):
        """Initialize the game board."""
        self.current_game_board_tuple = STARTING_BOARD
        self.previous_game_board_tuples_list = [self.current_game_board_tuple]

    def change_board(self, new_board_tuple: tuple):
        """Change current_game_board_tuple to new_board_tuple"""
        self.previous_game_board_tuples_list.append(self.current_game_board_tuple)
        self.current_game_board_tuple = new_board_tuple

    def try_undo_move(self):
        """Try to undo a move and return True if succeeded."""
        if len(self.previous_game_board_tuples_list) > 1:
            self.current_game_board_tuple = self.previous_game_board_tuples_list[-1]
            self.previous_game_board_tuples_list.remove(self.previous_game_board_tuples_list[-1])
            return True
        return False
