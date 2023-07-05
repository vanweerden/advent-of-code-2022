import sys
import unittest
import io
from main import *

class Day8Tests(unittest.TestCase):
    file = "test_input.txt"

    def test_matrix_from(self):
        matrix = matrix_from(self.file)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput     # redirect stdout
        matrix.print()
        sys.stdout = sys.__stdout__     # reset stdout redirect
        actual = capturedOutput.getvalue()

        expected = f'30373\n25512\n65332\n33549\n35390\n'
        self.assertEqual(actual, expected)

    def test_right_of(self):
        matrix = matrix_from(self.file)

        actual = matrix.right_of(1, 1)
        
        expected = [5, 1, 2]
        self.assertEqual(actual, expected)

    def test_right_of__right_edge(self):
        matrix = matrix_from(self.file)

        actual = matrix.right_of(4, 4)
        
        expected = []
        self.assertEqual(actual, expected)

    def test_left_of(self):
        matrix = matrix_from(self.file)

        actual = matrix.left_of(3, 3)
        
        expected = [5, 3, 3]
        self.assertEqual(actual, expected)

    def test_left_of__left_edge(self):
        matrix = matrix_from(self.file)

        actual = matrix.left_of(2, 0)
        
        expected = []
        self.assertEqual(actual, expected)


    def test_below(self):
        matrix = matrix_from(self.file)

        actual = matrix.below(0, 4)
        
        expected = [2, 2, 9, 0]
        self.assertEqual(actual, expected)

    def test_below__bottom_edge(self):
        matrix = matrix_from(self.file)

        actual = matrix.below(4, 1)
        
        expected = []
        self.assertEqual(actual, expected)

    def test_above(self):
        matrix = matrix_from(self.file)

        actual = matrix.above(4, 3)
        
        expected = [4, 3, 1, 7]
        self.assertEqual(actual, expected)

    def test_above__top_edge(self):
        matrix = matrix_from(self.file)

        actual = matrix.above(0, 3)
        
        expected = []
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()