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

        expected = f'3 0 3 7 3 \n2 5 5 1 2 \n6 5 3 3 2 \n3 3 5 4 9 \n3 5 3 9 0 \n\n'
        self.assertEqual(actual, expected)

    def test_get_row(self):
        matrix = matrix_from(self.file)
        actual = matrix.get_row(2)
        self.assertEqual(actual, [6, 5, 3, 3, 2])

    def test_get_col(self):
        matrix = matrix_from(self.file)
        actual = matrix.get_col(2)
        self.assertEqual(actual, [3, 5, 3, 5, 3])

    def test_is_visible_hor__middle__true(self):
        matrix = matrix_from(self.file)
        matrix.set_value(9, 0, 1)
        is_visible = matrix.is_visible_hor(1, 1)
        self.assertTrue(is_visible)

    def test_is_visible_hor__middle__false(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_hor(2, 2)
        self.assertFalse(is_visible)

    def test_is_visible_hor__left_edge__true(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_hor(1, 0)
        self.assertTrue(is_visible)

    def test_is_visible_hor__right_edge__true(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_hor(1, 4)
        self.assertTrue(is_visible)

    def test_is_visible_vert__middle__true(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_vert(1, 2)
        self.assertTrue(is_visible)

    def test_is_visible_vert__middle__false(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_vert(2, 2)
        self.assertFalse(is_visible)

    def test_is_visible_vert__top_edge__true(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_vert(0, 2)
        self.assertTrue(is_visible)

    def test_is_visible_vert__bottom_edge__true(self):
        matrix = matrix_from(self.file)
        is_visible = matrix.is_visible_vert(4, 1)
        self.assertTrue(is_visible)

    def test_count_visible_trees(self):
        matrix = matrix_from(self.file)
        tree_count = matrix.count_visible_trees()
        self.assertEqual(tree_count, 21)

    def test_is_visible__visible_hor_only__true(self):
        matrix = matrix_from(self.file)
        matrix.set_value(9, 0, 1)
        is_visible = matrix.is_visible(1, 1)
        self.assertTrue(is_visible)

    def test_is_visible__visible_vert_only__true(self):
        matrix = matrix_from(self.file)
        matrix.set_value(9, 1, 0)
        is_visible = matrix.is_visible(1, 1)
        self.assertTrue(is_visible)

# TEST: is_visible when visible horizontally but not vertically

if __name__ == '__main__':
    unittest.main()