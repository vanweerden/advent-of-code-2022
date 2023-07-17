class DynamicMatrix:
    def __init__(self, rows, cols):
        self._default_val = False
        self._matrix = [[self._default_val for _ in range(cols)] for _ in range(rows)]
        self._width = cols
        self._height = rows

    def set(self, row_index, col_index, val):
        # this assumes indices will only be 1 beyond max
        if row_index >= self._height:
            self.add_row()
        if col_index >= self._width:
            self.add_col()
        self._matrix[row_index][col_index] = val

    def add_row(self):
        self.matrix.append([self._default_val for _ in range(self._width)])
        self.calculate_height()

    def add_col(self):
        for row in self._matrix:
            row.append(self._default_val)
        self.calculate_width()

    def calculate_height(self):
        self._height = len(self._matrix)

    def calculate_width(self):
        self._width = len(self._matrix[0])

    def print(self):
        print()
        print("UPDATE")
        for row in self._matrix:
            for val in row:
                print(val, " ")
            print()