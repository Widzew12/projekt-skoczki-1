class Field:
    def __init__(self, row_index: int, column_index: int, board_tuple: tuple):
        self.row_index = row_index
        self.column_index = column_index
        self.content = board_tuple[row_index][column_index]
