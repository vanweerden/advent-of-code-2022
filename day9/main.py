from rope import Rope
from dynamic_matrix import DynamicMatrix
"""

Main:
0) Init rope at point 0,0 and init matrix with 0, 0 length and height
1) Feed all directions to rope
2) Each time head moves on step, update tail position and mark tail position in matrix
3) Count the number of positions the tail has visited at least once

CLASSES
- Rope 
    * METHOD: update tail position given head position
    * METHOD: move head given instruction and update tail position after each step
- Matrix to mark which positions tail has visited (simple mark as True)
    * allow dynamic addition of rows and columns
- I need to reverse rows: 0 is bottom row
"""

def get_lines(file):
        with open(file) as f:
            return f.read().splitlines()
        
def count_visited(matrix):
    total = 0
    for row in matrix:
        for val in row:
            if val == True:
                total += 1
    return total

def count_tail_positions(file):
    rope = Rope(0, 0, 0, 0)
    matrix = DynamicMatrix()
    lines = get_lines(file)

    for l in lines:
        direction = l.split(" ")[0]
        distance = int(l.split(" ")[1])

        for _ in range(distance):
            rope.move_head(direction)
            matrix.mark(rope.tail_row, rope.tail_col)

    return count_visited(matrix.matrix)

print("Part 1:", count_tail_positions("input.txt"))