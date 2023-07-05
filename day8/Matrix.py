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
    
    # create methods that return a list of values from a point to the edges
    # right
    def right_of(self, starting_row, starting_col):
        values = []
        for col in self._matrix[starting_row][starting_col:]:
            values.append(self._matrix[starting_row][col])
        return values

    def left_of(self, starting_row, end_col):
        values = []
        for col in reversed(self._matrix[starting_row][:end_col]):
            values.append(self._matrix[starting_row][col])
        return []

    def above(self, starting_row, starting_col):
        return []
    
    def below(self, starting_row, starting_col):
        return []
        
    # TODO: Diagonal methods