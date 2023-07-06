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
   
    def is_visible_hor(self, row_index, col_index):
        # Trees on edge are always visible
        if col_index == 0 or col_index == self._width-1:
            return True
        else:
            row = self.get_row[row_index]
            tree_height = self.get_value(row_index, col_index)
            # Remove tree in question from row
            other_trees = row[:col_index] + row[col_index+1:]
            is_visible = True
            for t in other_trees:
                if t >= tree_height:
                    is_visible = False
            return is_visible
        
    def is_visible_vert(self, row_index, col_index):
        # Trees on edge are always visible
        if row_index == 0 or row_index == self._height-1:
            return True
        else:
            col = self.get_col[col_index]
            tree_height = self.get_value(row_index, col_index)
            # Remove tree in question from col
            other_trees = col[:row_index] + col[row_index+1:]
            is_visible = True
            for t in other_trees:
                if t >= tree_height:
                    is_visible = False
            return is_visible
        
    # def count_visible_trees():

    # TODO: 
    # 1. Get tests to pass
    # 2. Add count_visible_trees function and solve problem
    # 3. Refactor: is_visible_hor and is_visible_vert repeat steps. Can I extract code to new method?