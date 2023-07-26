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

        # if either row or col is 2 or more spaces away
        if (self.is_not_adjacent(row_diff, col_diff)):
            # move col and row one space in direction of diff
            new_row = self.get_row(curr_knot) + self.direction_from(row_diff)
            new_col = self.get_col(curr_knot) + self.direction_from(col_diff)
            self.set_pos(knot_index, new_row, new_col)

    def direction_from(self, diff):
        if diff < 0:
            return -1
        elif diff > 0:
            return 1
        else:
            return 0

    def get_row(self, knot):
        return knot[0]

    def get_col(self, knot):
        return knot[1]

    def get_head(self):
        return self._knots[0]

    def get_tail(self):
        return self._knots[len(self._knots)-1]

    def set_head(self, row, col):
        self.set_pos(0, row, col)

    def set_pos(self, knot_index, row, col):
        self._knots[knot_index][0] = row
        self._knots[knot_index][1] = col
    
    def is_not_adjacent(self, row_diff, col_diff):
        return abs(col_diff) >= 2 or abs(row_diff) >= 2

    def move_to_left_of_prev(self, knot_index):
        curr_row = self.get_row(self._knots[knot_index])
        prev_col = self.get_col(self._knots[knot_index-1])
        self.set_pos(knot_index, curr_row, prev_col-1)

    def move_to_right_of_prev(self, knot_index):
        curr_row = self.get_row(self._knots[knot_index])
        prev_col = self.get_col(self._knots[knot_index-1])
        self.set_pos(knot_index, curr_row, prev_col+1)

    def move_above_prev(self, knot_index):
        prev_row = self.get_row(self._knots[knot_index-1])
        curr_col = self.get_col(self._knots[knot_index])
        self.set_pos(knot_index, prev_row-1, curr_col)

    def move_below_prev(self, knot_index):
        prev_row = self.get_row(self._knots[knot_index-1])
        curr_col = self.get_col(self._knots[knot_index])
        self.set_pos(knot_index, prev_row+1, curr_col)