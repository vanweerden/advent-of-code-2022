class Rope:
    def __init__(self, head_row, head_col, tail_row, tail_col):
        self.head_row = head_row
        self.head_col = head_col
        self.tail_row = tail_row
        self.tail_col = tail_col

    def move_head(self, direction):
        if direction == "R":
            self.head_col += 1
        elif direction == "L":
            self.head_col -= 1
        # "up" and "down" are reversed so the "bottom" row is row 0
        elif direction == "D":
            self.head_row -= 1
        elif direction == "U":
            self.head_row += 1

        self.update_tail_pos()

    def update_tail_pos(self):
        col_diff = self.head_col - self.tail_col
        row_diff = self.head_row - self.tail_row

        if (self.is_left_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_to_left_of_head()
        elif (self.is_right_and_not_adjacent(row_diff, col_diff)):
            self.tail_col = self.head_col+1
            self.move_tail_to_right_of_head()
        elif (self.is_above_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_above_head()
        elif (self.is_below_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_below_head()

    def is_left_and_not_adjacent(self, row_diff, col_diff):
        return abs(row_diff) <= 1 and col_diff == 2

    def is_right_and_not_adjacent(self, row_diff, col_diff):
        return abs(row_diff) <= 1 and col_diff == -2

    def is_below_and_not_adjacent(self, row_diff, col_diff):
        return abs(col_diff) <= 1 and row_diff == -2

    def is_above_and_not_adjacent(self, row_diff, col_diff):
        return abs(col_diff) <= 1 and row_diff == 2

    def move_tail_to_left_of_head(self):
        self.tail_row = self.head_row 
        self.tail_col = self.head_col-1

    def move_tail_to_right_of_head(self):
        self.tail_row = self.head_row 
        self.tail_col = self.head_col+1

    def move_tail_above_head(self):
        self.tail_row = self.head_row-1 
        self.tail_col = self.head_col

    def move_tail_below_head(self):
        self.tail_row = self.head_row+1 
        self.tail_col = self.head_col