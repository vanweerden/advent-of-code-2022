class DynamicMatrix:
    def __init__(self, rows=0, cols=0):
        self._empty_val = False
        self._mark_val = True
        self.matrix = [] if rows == 0 or cols == 0 else [[self._empty_val for _ in range(cols)] for _ in range(rows)]
        self._width = cols
        self._height = rows

    def mark(self, row_index, col_index):
        # this assumes indices will only be 1 beyond max
        if row_index >= self._height:
            self.add_row()
        if col_index >= self._width:
            self.add_col()
        self.matrix[row_index][col_index] = self._mark_val

    def add_row(self):
        self.matrix.append([self._empty_val for _ in range(self._width)])
        self.calculate_height()

    def add_col(self):
        for row in self.matrix:
            row.append(self._empty_val)
        self.calculate_width()

    def calculate_height(self):
        self._height = len(self.matrix)

    def calculate_width(self):
        self._width = len(self.matrix[0])

    def print(self):
        print()
        # reversed to treat row 0 as the "bottom" row
        for row in reversed(self.matrix):
            for col in row:
                print(col, end=" ")
            print()
        print()