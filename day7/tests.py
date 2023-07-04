import unittest
from main import *

class Day7Tests(unittest.TestCase):
    tree = file_tree_from("test_input.txt")

    def solve_part_1(self):
        actual = solve_part_1(self.tree)
        expected = 95437
        self.assertEqual(actual, expected)  

    def test_get_unused_space(self):
        actual = get_unused_space(self.tree)
        expected = 21618835
        self.assertEqual(actual, expected)   

    def test_get_space_to_free(self):
        unused_space = 21618835
        actual = get_space_to_free(unused_space)
        expected = 8381165
        self.assertEqual(actual, expected)

    def test_solve_part_2(self):
        actual = solve_part_2(self.tree)
        expected = 24933642
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()