from game_board import GameBoard
from field import Field
from move import Move


def print_board():
    print("-----------------------------------------------------------------")
    for row in game_board.current_game_board_tuple:
        output_row = "| "
        for field_content in row:
            output_row += field_content + " | "
        print(output_row)
        print("-----------------------------------------------------------------")


if __name__ == '__main__':
    game_board = GameBoard()

    print_board()

    start_row_index = int(input("start row index: "))
    start_column_index = int(input("start column index: "))
    target_row_index = int(input("target row index: "))
    target_column_index = int(input("target column index: "))
    start_field = Field(start_row_index, start_column_index, game_board.current_game_board_tuple)
    target_field = Field(target_row_index, target_column_index, game_board.current_game_board_tuple)

    move = Move(start_field, target_field, game_board)
    move.check_and_make_move()
    new_board_tuple = move.new_board_tuple
    game_board.change_board(new_board_tuple)

    print_board()

