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
                print(f'{col}:{"T" if self.is_visible(row_index, col_index) else "F"} ', end="")
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
            tree_height = self.get_value(row_index, col_index)
            is_visible_left = self.is_visible_in(tree_height, self.get_left_slice(row_index, col_index))
            is_visible_right = self.is_visible_in(tree_height, self.get_right_slice(row_index, col_index))
            return is_visible_left or is_visible_right
        
    def get_left_slice(self, row_index, col_index):
        row = self.get_row(row_index)
        left_slice = row[:col_index]
        left_slice.reverse()
        return left_slice

    def get_right_slice(self, row_index, col_index):
        row = self.get_row(row_index)
        return row[col_index+1:]
    
    def is_visible_vert(self, row_index, col_index):
        # Trees on edge are always visible
        if row_index == 0 or row_index == self._height-1:
            return True
        else:
            tree_height = self.get_value(row_index, col_index)
            is_visible_above = self.is_visible_in(tree_height, self.get_upper_slice(row_index, col_index))
            is_visible_below = self.is_visible_in(tree_height, self.get_lower_slice(row_index, col_index))

            return is_visible_above or is_visible_below

    def get_upper_slice(self, row_index, col_index):
        col = self.get_col(col_index)
        upper_slice = col[:row_index]
        upper_slice.reverse()
        return upper_slice

    def get_lower_slice(self, row_index, col_index):
        col = self.get_col(col_index)
        return col[row_index+1:]
    
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
    
    def count_visible_trees_from(self, row_index, col_index, slice):
        tree_height = self.get_value(row_index, col_index)

        count = 0
        for t in slice:
            if t >= tree_height:
                # count the last visible tree
                count += 1
                break
            else:
            # count all trees smaller than this one
                count += 1 
        return count
    
    def count_trees_above(self, row_index, col_index):
        upper_slice = self.get_upper_slice(row_index, col_index)
        return self.count_visible_trees_from(row_index, col_index, upper_slice)
    
    def count_trees_below(self, row_index, col_index):
         return self.count_visible_trees_from(row_index, col_index, self.get_lower_slice(row_index, col_index))
        
    def count_trees_on_right(self, row_index, col_index):
        return self.count_visible_trees_from(row_index, col_index, self.get_right_slice(row_index, col_index))
        
    def count_trees_on_left(self, row_index, col_index):
        return self.count_visible_trees_from(row_index, col_index, self.get_left_slice(row_index, col_index))

    def calculate_scenic_score(self, row_index, col_index):
        trees_above = self.count_trees_above(row_index, col_index)
        trees_below = self.count_trees_below(row_index, col_index)
        trees_on_right = self.count_trees_on_right(row_index, col_index)
        trees_on_left = self.count_trees_on_left(row_index, col_index)
        print(trees_above, trees_below, trees_on_right, trees_on_left)
        return trees_above * trees_below * trees_on_right * trees_on_left