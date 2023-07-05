class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        self._width = cols
        self._height = rows

    def print(self):
        for row in self._matrix:
            for col in row:
                print(col, end="")
            print()

    def add_value(self, val, row_index, col_index):
        self._matrix[row_index][col_index] = val

    def get_value(self, row_index, col_index):
        return self._matrix[row_index][col_index]
    
    def right_of(self, row, starting_col):
        return self._matrix[row][starting_col+1:]

    def left_of(self, row, end_col):
        return list(reversed(self._matrix[row][:end_col]))

    def below(self, starting_row, col):
        values = []
        for row in self._matrix[starting_row+1:]:
            values.append(row[col])
        return values

    def above(self, starting_row, col):
        values = []
        for row in reversed(self._matrix[:starting_row]):
            values.append(row[col])
        return values
        
    # TODO: Diagonal methods