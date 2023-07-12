class Rope:
    def __init__(self, head_x, head_y, tail_x, tail_y):
        self.head_x = head_x
        self.head_y = head_y
        self.tail_x = tail_x
        self.tail_y = tail_y

    def tail_is_touching_head(self):
        x_check = abs(self.tail_x - self.head_x) < 2
        y_check = abs(self.tail_y - self.head_y) < 2
        return x_check and y_check
    
    def move_head(self, direction):
        # takes direction ("R 4"), parses it, and moves the head into that position
        # move tail automatically
        self.update_tail_pos()        

    def update_tail_pos(self):
        # same row and col is 2+ steps away => tail_x goes adjacent to head_x
        # same col and row is 2+ steps away => tail_y goes adjecent to head_y
        # TODO: figure out diagonal
