from rope import Rope
from dynamic_matrix import DynamicMatrix

def get_lines(file):
        with open(file) as f:
            return f.read().splitlines()
        
def count_visited(matrix):
    total = 0
    for row in matrix.keys():
        for val in matrix[row].values():
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
            if rope.head_row > 0 or rope.head_col > 0:
                matrix.mark(rope.tail_row, rope.tail_col)

    return count_visited(matrix.matrix)

# TODO: Answer is too low!
print("Part 1:", count_tail_positions("input.txt"))