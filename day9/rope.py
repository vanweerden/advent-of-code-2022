class Rope:
    def __init__(self, length):
        # [[row, col], [row, col], [row, col]]
        self._knots = []
        for _ in range(length):
            self._knots.append([0, 0])

    def move_head(self, direction):
        if direction == "R":
            self._knots[0][1] += 1
        elif direction == "L":
            self._knots[0][1] -= 1
        # "up" and "down" are reversed so the "bottom" row is row 0
        elif direction == "D":
            self._knots[0][0] -= 1
        elif direction == "U":
            self._knots[0][0] += 1

        for i in range(1, len(self._knots)):
            self.update_pos(i)

    def update_pos(self, knot_index):
        curr_knot = self._knots[knot_index]
        prev_knot = self._knots[knot_index-1]
        col_diff = self.get_col(prev_knot) - self.get_col(curr_knot)
        row_diff = self.get_row(prev_knot) - self.get_row(curr_knot)

        if (self.is_left_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_to_left_of_head()
        elif (self.is_right_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_to_right_of_head()
        elif (self.is_above_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_above_head()
        elif (self.is_below_and_not_adjacent(row_diff, col_diff)):
            self.move_tail_below_head()

    def get_row(self, knot):
        return knot[0]

    def get_col(self, knot):
        return knot[1]

    def get_head(self):
        return self._knots[0]

    def get_tail(self):
        return self._knots[len(self._knots)-1]

    def set_head(self, row, col):
        self._knots[0][0] = row
        self._knots[0][1] = col

    def set_tail(self, row, col):
        self._knots[len(self._knots)-1][0] = row
        self._knots[len(self._knots)-1][1] = col
    
    def is_left_and_not_adjacent(self, row_diff, col_diff):
        return abs(row_diff) <= 1 and col_diff == 2

    def is_right_and_not_adjacent(self, row_diff, col_diff):
        return abs(row_diff) <= 1 and col_diff == -2

    def is_below_and_not_adjacent(self, row_diff, col_diff):
        return abs(col_diff) <= 1 and row_diff == -2

    def is_above_and_not_adjacent(self, row_diff, col_diff):
        return abs(col_diff) <= 1 and row_diff == 2

    def move_tail_to_left_of_head(self):
        new_row = self.get_row(self.get_head())
        new_col = self.get_col(self.get_head())-1
        self.set_tail(new_row, new_col)

    def move_tail_to_right_of_head(self):
        new_row = self.get_row(self.get_head()) 
        new_col = self.get_col(self.get_head())+1
        self.set_tail(new_row, new_col)

    def move_tail_above_head(self):
        new_row = self.get_row(self.get_head())-1 
        new_col = self.get_col(self.get_head())
        self.set_tail(new_row, new_col)

    def move_tail_below_head(self):
        new_row = self.get_row(self.get_head())+1 
        new_col = self.get_col(self.get_head())
        self.set_tail(new_row, new_col)