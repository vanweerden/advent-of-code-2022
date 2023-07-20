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
    rope = Rope(2)
    matrix = DynamicMatrix()
    lines = get_lines(file)

    for l in lines:
        direction = l.split(" ")[0]
        distance = int(l.split(" ")[1])

        for _ in range(distance):
            rope.move_head(direction)
            tail = rope.get_tail()
            print(tail)
            matrix.mark(tail[0], tail[1])

    return count_visited(matrix.matrix)

# print("Part 1:", count_tail_positions("input.txt"))

# PART 2
# rope is how 10 knots long!
# each knot behaves like the tail in part 1 when the knot ahead of it moves
# 
# (x) amend Rope so you can choose length
# (2) get tests to pass
# (3) when head moves, update all points in rope
# (4) the tail is the last point: track this as usual


""" LEARNINGS
1. A matrix can be made out of dictionaries rather than lists. This lets you (1) dynamically add rows and columns, and (2) add rows and cols to negative indices.
2. Tuples cannot be assigned to. Use lists instead. Think of tuples as constants.
"""