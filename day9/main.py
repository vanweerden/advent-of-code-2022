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

def count_tail_positions(file, rope_size):
    rope = Rope(rope_size)
    matrix = DynamicMatrix()
    lines = get_lines(file)

    for l in lines:
        direction = l.split(" ")[0]
        distance = int(l.split(" ")[1])

        for _ in range(distance):
            rope.move_head(direction)
            tail = rope.get_tail()
            matrix.mark(tail[0], tail[1])

    return count_visited(matrix.matrix)

# print("Part 1:", count_tail_positions("input.txt"), 2)
# print("Part 2:", count_tail_positions("input.txt"), 10)
# PART 2



""" LEARNINGS
1. A matrix can be made out of dictionaries rather than lists. This lets you (1) dynamically add rows and columns, and (2) add rows and cols to negative indices.
2. Tuples cannot be assigned to. Use lists instead. Think of tuples as constants.
"""