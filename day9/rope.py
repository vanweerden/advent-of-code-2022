class Rope:
    def __init__(self, head_row, head_col, tail_row, tail_col):
        self.head_row = head_row
        self.head_col = head_col
        self.tail_row = tail_row
        self.tail_col = tail_col

    # def tail_is_touching_head(self):
    #     x_check = abs(self.tail_row - self.head_row) < 2
    #     y_check = abs(self.tail_col - self.head_col) < 2
    #     return x_check and y_check
    
    def move_head(self, direction):
        # takes direction ("R 4"), parses it, and moves the head into that position
        # move tail automatically
        self.update_tail_pos()        

    def update_tail_pos(self):
        col_diff = self.head_col - self.tail_col
        row_diff = self.head_row - self.tail_row

        # same row and col is 2+ steps away => tail_row goes adjacent to head_row
        if (row_diff == 0 and col_diff >= 2):
            # move to left of head
            self.tail_col = self.head_col-1
        # same row: tail is 2+ spaces to the left
        elif (row_diff == 0 and col_diff <= -2):
            self.tail_col = self.head_col+1

        # same col: tail is 2+ spaces above
        elif (col_diff == 0 and row_diff >= 2):
            # move above head
            self.tail_row = self.head_row-1
        # same col: tail is 2+ spaces below
        elif (col_diff == 0 and row_diff <= -2):
            self.tail_row = self.head_row+1

        
        # same col and row is 2+ steps away => tail_col goes adjecent to head_col
        # TODO: figure out diagonal
