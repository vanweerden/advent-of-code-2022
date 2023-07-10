from Matrix import Matrix

def matrix_from(file):
    with open(file) as f:
        lines = f.read().splitlines()
    
    height = len(lines)
    width = len(lines[0])
    matrix = Matrix(height, width)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix.set_value(int(char), i, j)
    return matrix

# file = "input.txt"
# matrix = matrix_from(file)
# print("Part 1:", matrix.count_visible_trees())
# print("Part 2:", matrix.get_highest_scenic_score())