class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        self._width = cols
        self._height = rows

    def print(self):
        for row in self._matrix:
            for col in row:
                print(col, end=" ")
            print()
        print()

    def print_visibility(self):
        for row_index, row in enumerate(self._matrix):
            for col_index, col in enumerate(row):
                print("T " if self.is_visible(row_index, col_index) else "F ", end="")
            print()
        print()

    def set_value(self, val, row_index, col_index):
        self._matrix[row_index][col_index] = val

    def get_value(self, row_index, col_index):
        return self._matrix[row_index][col_index]
    
    def get_row(self, row_index):
        return self._matrix[row_index]
    
    def get_col(self, col_index):
        values = []
        for row in self._matrix:
            values.append(row[col_index])
        return values

    def is_visible(self, row_index, col_index):
        return self.is_visible_vert(row_index, col_index) or self.is_visible_hor(row_index, col_index)
   
    def is_visible_hor(self, row_index, col_index):
        # Trees on edge are always visible
        if col_index == 0 or col_index == self._width-1:
            return True
        else:
            row = self.get_row(row_index)
            tree_height = self.get_value(row_index, col_index)
            is_visible_right = self.is_visible_in(tree_height, row[:col_index])
            is_visible_right = self.is_visible_in(tree_height, row[col_index+1:])
   
            return is_visible_right or is_visible_right
        
    def is_visible_vert(self, row_index, col_index):
        # Trees on edge are always visible
        if row_index == 0 or row_index == self._height-1:
            return True
        else:
            col = self.get_col(col_index)
            tree_height = self.get_value(row_index, col_index)
            is_visible_above = self.is_visible_in(tree_height, col[:row_index])
            is_visible_below = self.is_visible_in(tree_height, col[row_index+1:])

            return is_visible_above or is_visible_below

    def is_visible_in(self, val, collection):
        is_greater = True
        for x in collection:
            if x >= val:
                is_greater = False
        return is_greater

    def count_visible_trees(self):
        count = 0
        for row_index, row in enumerate(self._matrix):
            for col_index, tree in enumerate(row):
                if self.is_visible(row_index, col_index):
                    count += 1
        return count