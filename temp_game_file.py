# NONE = 0
# WHITE = 1
# BLACK = 2
# EMPTY = 3
# STARTING_BOARD = ([NONE, BLACK, NONE, BLACK, NONE, BLACK, NONE, BLACK],
#                   [BLACK, NONE, BLACK, NONE, BLACK, NONE, BLACK, NONE],
#                   [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#                   [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#                   [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#                   [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#                   [NONE, WHITE, NONE, WHITE, NONE, WHITE, NONE, WHITE],
#                   [WHITE, NONE, WHITE, NONE, WHITE, NONE, WHITE, NONE])
# END_BOARD = ([NONE, WHITE, NONE, WHITE, NONE, WHITE, NONE, WHITE],
#              [WHITE, NONE, WHITE, NONE, WHITE, NONE, WHITE, NONE],
#              [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#              [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#              [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#              [NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE],
#              [NONE, BLACK, NONE, BLACK, NONE, BLACK, NONE, BLACK],
#              [BLACK, NONE, BLACK, NONE, BLACK, NONE, BLACK, NONE])
# FIELD_NAMES = (('A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'),
#                ('A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'),
#                ('A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'),
#                ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'),
#                ('A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'),
#                ('A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'),
#                ('A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'),
#                ('A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'))
# OUTPUT_TEMPLATE = ((EMPTY, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', EMPTY),
#                    ['8', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '8'],
#                    ['7', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '7'],
#                    ['6', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '6'],
#                    ['5', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '5'],
#                    ['4', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '4'],
#                    ['3', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '3'],
#                    ['2', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '2'],
#                    ['1', NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, '1'],
#                    (EMPTY, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', EMPTY))
# ROW_LENGTH = 8
# COLUMN_LENGTH = 8
# SEPARATING_STRING = '-----------------------------------------'
# ANSWER_YES = 'y'
# ANSWER_NO = 'n'
#
#
# class GameBoard:
#     def __init__(self):
#         self.board = STARTING_BOARD
#
#     def change_field(self, field):
#         self.board[field.row_index][field.column_index] = field.content.value
#
#     def print_board(self):
#         temp_board = OUTPUT_TEMPLATE
#         for row_index in range(ROW_LENGTH):
#             for column_index in range(COLUMN_LENGTH):
#                 field = Field(row_index, column_index, self)
#                 temp_board[row_index + 1][column_index + 1] = field.content.value
#
#         string_board = change_indexes_to_symbols(temp_board)
#
#         output_board = []
#         for row in string_board:
#             output_board.append(SEPARATING_STRING)
#             output_string = '| '
#             for field in row:
#                 output_string += field + ' | '
#             output_board.append(output_string)
#         output_board.append(SEPARATING_STRING)
#
#         for row in output_board:
#             print(row)
#
#
# class FieldNamesBoard:
#     def __init__(self):
#         self.board = FIELD_NAMES
#
#     def find_field_by_name(self, field_name, game_board: GameBoard):
#         for row_index in range(ROW_LENGTH):
#             for column_index in range(COLUMN_LENGTH):
#                 field_names_field = Field(row_index, column_index, self)
#                 if field_name == field_names_field.content:
#                     output_field = Field(row_index, column_index, game_board)
#                     return output_field
#         return False
#
#
# class Field:
#     def __init__(self, row_index: int, column_index: int, board: (GameBoard, FieldNamesBoard)):
#         self.row_index = row_index
#         self.column_index = column_index
#         content = board.board[row_index][column_index]
#         self.content = FieldContent(content)
#         # self.content = board.board[row_index][column_index]
#
#
# class FieldContent:
#     def __init__(self, value):
#         self.value = value
#
#     def get_content_string(self):
#         if check_if_game_field(self.value):
#             if self.value == NONE:
#                 return 'N'
#             elif self.value == WHITE:
#                 return 'W'
#             elif self.value == BLACK:
#                 return 'B'
#             elif self.value == EMPTY:
#                 return ' '
#             return None
#         return self.value
#
#
# def try_make_game_field(row_index: int, column_index: int, board: GameBoard):
#     if check_for_valid_index(row_index, column_index):
#         output_field = Field(row_index, column_index, board)
#         return output_field
#     return False
#
#
# def check_if_game_field(field_content):
#     if type(field_content) is int:
#         return True
#     return False
#
#
# def print_wrong_field_message():
#     print('You entered a wrong field or your entry is not a field.')
#
#
# # def change_content_to_symbol(field_content: int):
# #     if field_content == NONE:
# #         return 'N'
# #     elif field_content == WHITE:
# #         return 'W'
# #     elif field_content == BLACK:
# #         return 'B'
# #     elif field_content == EMPTY:
# #         return ' '
# #     else:
# #         return None
#
#
# def change_indexes_to_symbols(input_board):
#     output_board = []
#     for row in input_board:
#         new_row = []
#         for field in row:
#             field_content = field
#             if check_if_game_field(field_content):
#                 new_field_content = change_content_to_symbol(field_content)
#                 new_row.append(new_field_content)
#             else:
#                 new_row.append(field_content)
#         output_board.append(new_row)
#     return output_board
#
#
# # def print_game_board(input_board):
# #     temp_board = OUTPUT_TEMPLATE
# #     for row_index in range(ROW_LENGTH):
# #         for column_index in range(COLUMN_LENGTH):
# #             field = Field(row_index, column_index, input_board)
# #             temp_board[row_index + 1][column_index + 1] = field.content
# #
# #     string_board = change_indexes_to_symbols(temp_board)
# #
# #     output_board = []
# #     for row in string_board:
# #         output_board.append(SEPARATING_STRING)
# #         output_string = '| '
# #         for field in row:
# #             output_string += field + ' | '
# #         output_board.append(output_string)
# #     output_board.append(SEPARATING_STRING)
# #
# #     for row in output_board:
# #         print(row)
#
#
# def find_field_content(field, board):
#     return board[field.row_index][field.column_index]
#     # return board[field_row_index][field_column_index]
#
#
# def check_neighbouring_fields(input_field, board):
#     output_list = []
#
#     field_1_row_index = input_field.row_index - 1
#     field_1_column_index = input_field.column_index - 1
#     field_1 = try_make_game_field(field_1_row_index, field_1_column_index, board)
#     if field_1:
#         output_list.append(field_1)
#
#     field_2_row_index = input_field.row_index + 1
#     field_2_column_index = input_field.column_index - 1
#     field_2 = try_make_game_field(field_2_row_index, field_2_column_index, board)
#     if field_2:
#         output_list.append(field_2)
#
#     field_3_row_index = input_field.row_index - 1
#     field_3_column_index = input_field.column_index + 1
#     field_3 = try_make_game_field(field_3_row_index, field_3_column_index, board)
#     if field_3:
#         output_list.append(field_3)
#
#     field_4_row_index = input_field.row_index + 1
#     field_4_column_index = input_field.column_index + 1
#     field_4 = try_make_game_field(field_4_row_index, field_4_column_index, board)
#     if field_4:
#         output_list.append(field_4)
#
#     return output_list
#
#
# def check_for_valid_index(row_index, column_index):
#     output_bool = 0 <= row_index < ROW_LENGTH and 0 <= column_index < COLUMN_LENGTH
#     return output_bool
#
#
# def check_move(start_field, target_field, board):
#     # Check if it is not the same field
#     if start_field.row_index == target_field.row_index and start_field.column_index == target_field.column_index:
#         return False
#     # Check if the target field is empty
#     if target_field.value != NONE:
#         return False
#     # Check if the move is by 1 or more fields
#     if ((start_field.row_index == target_field.row_index - 1 or start_field.row_index == target_field.row_index + 1) and
#             (start_field.column_index == target_field.column_index - 1 or start_field.column_index == target_field.column_index + 1)):
#         new_board = move_by_one(start_field, target_field, board)
#         return new_board
#     else:
#         new_board = move_by_more_than_one(start_field, target_field, board)
#         return new_board
#
#
# def check_additional_move(start_field, target_field, possible_targets, board):
#     pass
#
#
# def move_by_one(start_field, target_field, board):
#     pawn_color = start_field.value
#     board[target_field.row_index][target_field.column_index] = pawn_color
#     board[start_field.row_index][start_field.column_index] = NONE
#     return board
#
#
# def move_by_more_than_one(start_field, target_field, board):
#     pawn_color = start_field.value
#     # Check if the move is performed diagonally
#     if ((start_field.row_index == target_field.row_index + 2 or start_field.row_index == target_field.row_index - 2) and
#             (start_field.column_index == target_field.column_index + 2 or start_field.column_index == target_field.column_index - 2)):
#         middle_field = find_middle_field(start_field, target_field, board)
#         if not middle_field:
#             return False
#         middle_pawn_color = middle_field.content
#         if middle_pawn_color == WHITE or middle_pawn_color == BLACK:
#             board[target_field.row_index][target_field.column_index] = pawn_color
#             board[start_field.row_index][start_field.column_index] = NONE
#             valid_additional_moves = check_for_more_moves(target_field, start_field, board)
#             if not valid_additional_moves:
#                 return board
#             new_board = make_additional_move(target_field, valid_additional_moves, board)
#             if not new_board:
#                 return board
#             return new_board
#     return False
#
#
# def find_middle_field(start_field, target_field, board):
#     middle_field_row_index = (start_field.row_index + target_field.row_index) / 2
#     middle_field_column_index = (start_field.column_index + target_field.column_index) / 2
#     # Check if the middle field index is an integer - if it isn't, then the middle field doesn't exist.
#     if not (middle_field_row_index.is_integer() or middle_field_column_index.is_integer()):
#         return False
#     middle_field_row_index = int(middle_field_row_index)
#     middle_field_column_index = int(middle_field_column_index)
#     output_field = Field(middle_field_row_index, middle_field_column_index, board)
#     return output_field
#
#
# def check_for_more_moves(start_field, previous_field, board):
#     valid_moves = []
#     field_1_row_index = start_field.row_index - 2
#     field_1_column_index = start_field.column_index - 2
#     field_1 = try_make_game_field(field_1_row_index, field_1_column_index, board)
#     if field_1:
#         if check_for_long_move(start_field, field_1, previous_field, board):
#             valid_moves.append(field_1)
#     field_2_row_index = start_field.row_index + 2
#     field_2_column_index = start_field.column_index - 2
#     field_2 = try_make_game_field(field_2_row_index, field_2_column_index, board)
#     if field_2:
#         if check_for_long_move(start_field, field_2, previous_field, board):
#             valid_moves.append(field_2)
#     field_3_row_index = start_field.row_index - 2
#     field_3_column_index = start_field.column_index + 2
#     field_3 = try_make_game_field(field_3_row_index, field_3_column_index, board)
#     if field_3:
#         if check_for_long_move(start_field, field_3, previous_field, board):
#             valid_moves.append(field_3)
#     field_4_row_index = start_field.row_index + 2
#     field_4_column_index = start_field.column_index + 2
#     field_4 = try_make_game_field(field_4_row_index, field_4_column_index, board)
#     if field_4:
#         if check_for_long_move(start_field, field_4, previous_field, board):
#             valid_moves.append(field_4)
#     if len(valid_moves):
#         return valid_moves
#     return False
#
#
# def check_for_long_move(start_field, target_field, previous_field, board):
#     if not (target_field.row_index == previous_field.row_index and target_field.column_index == previous_field.column_index):
#         middle_field = find_middle_field(start_field, target_field, board)
#         if target_field.value == NONE and (middle_field.content == WHITE or middle_field.content == BLACK):
#             return True
#     return False
#
#
# def check_for_win(board):
#     pass
#
#
# def change_turn(turn):
#     if turn == WHITE:
#         return BLACK
#     elif turn == BLACK:
#         return WHITE
#     else:
#         return None
#
#
# def make_move(board, turn):
#     field_names_board = FieldNamesBoard()
#     print(f"{change_content_to_symbol(turn)}'s move")
#     while True:
#         start_field_name = input('Enter your starting field: ')
#         start_field = field_names_board.find_field_by_name(start_field_name, board)
#         if not start_field:
#             print_wrong_field_message()
#             continue
#         if start_field.content != turn:
#             print_wrong_field_message()
#             continue
#         break
#
#     while True:
#         target_field_name = input('Enter your target field: ')
#         target_field = field_names_board.find_field_by_name(target_field_name, board)
#         if not target_field:
#             print_wrong_field_message()
#             continue
#         new_board = check_move(start_field, target_field, board)
#         if not new_board:
#             print_wrong_field_message()
#             continue
#         break
#
#     print(check_neighbouring_fields(start_field, board))
#     print(check_neighbouring_fields(target_field, board))
#
#
# def make_additional_move(start_field, possible_targets, board):
#     answer = input(f'Would you like to make another move? {ANSWER_YES}/{ANSWER_NO}: ')
#     if answer == ANSWER_NO:
#         return False
#     return board
#
#
# def initialize_game_board():
#     output_list = STARTING_BOARD
#     return output_list
#
#
# if __name__ == '__main__':
#     game_board = GameBoard()
#     # game_board = initialize_game_board()
#     current_turn = WHITE
#
#     while True:
#         game_board.print_board()
#         make_move(game_board, current_turn)
#         current_turn = change_turn(current_turn)
