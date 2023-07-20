class DynamicMatrix:
    def __init__(self):
        self._empty_val = False
        self._mark_val = True
        self.matrix = { 0: { 0: self._mark_val }}

    def mark(self, row_index, col_index):
        if row_index not in self.matrix:
            self.add_row(row_index)
        if col_index not in self.matrix[row_index]:
            self.add_col(col_index)
        self.matrix[row_index][col_index] = self._mark_val

    def add_row(self, index):
        new_row = dict([(i, self._empty_val) for i in self.get_column_indices()])
        self.matrix[index] = new_row

    def add_col(self, index):
        for row in self.matrix.keys():
            self.matrix[row][index] = self._empty_val

    def get_column_indices(self):
        # Assumes there will always be a 0th row
        return list(self.matrix[0].keys())
    
    def get_max_col(self):
        return max(self.matrix[0].keys())
    
    def get_max_row(self):
        return max(self.matrix.keys())

    def print(self):
        print()
        # reversed to treat row 0 as the "bottom" row
        for row in reversed(self.matrix.keys()):
            for col in self.matrix[row].values():
                print(col, end=" ")
            print()
        print()