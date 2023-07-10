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

file = "input.txt"
matrix = matrix_from(file)
print("Part 1:", matrix.count_visible_trees())
print("Part 2:", matrix.test_get_hightest_scenic_score())
"""
PART 2
1) For each tree in the grid, count how many trees are greater than or equal to it (the tree that blocks its view) in each direction
2) multiply these together
3) find the tree with the highest score 

CHANGES NEEDED
x) extract methods to get sub-lists from a row or a column on either side of a tree (and reverses the top and left sub-lists)
x) four new methods to count visible trees from a given tree using methods from a)
x) new method that calculates a tree's scenic_score score by calling all four methods from b)
d) method to iterate over matrix and find the largest score

REFACTOR: Refactor old methods to use new ones (tree is visible if count of visible trees in one direction is 0)
"""