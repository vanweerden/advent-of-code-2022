class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def print(self):
        for row in self._matrix:
            for col in row:
                print(col, end="")
            print()

    def add_value(self, val, row_index, col_index):
        self._matrix[row_index][col_index] = val

    def get_value(self, row_index, col_index):
        return self._matrix[row_index][col_index]