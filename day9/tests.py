import sys
import unittest
from main import *
from rope import Rope

class DayNineTests(unittest.TestCase):
    file = "test_input.txt"

    def test_tail_is_touching_head__not_touching_hor__false(self):
        rope = Rope(1, 1, 1, 3)
        self.assertEqual(rope.tail_is_touching_head(), False)

    def test_tail_is_touching_head__not_touching_vert__false(self):
        rope = Rope(1, 1, 3, 1)
        self.assertEqual(rope.tail_is_touching_head(), False)

    def test_tail_is_touching_head__not_touching_diag__false(self):
        rope = Rope(1, 1, 2, 3)
        self.assertEqual(rope.tail_is_touching_head(), False)

    def test_tail_is_touching_head__touching_hor__true(self):
        rope = Rope(1, 1, 1, 2)
        self.assertEqual(rope.tail_is_touching_head(), True)

    def test_tail_is_touching_head__touching_vert__true(self):
        rope = Rope(1, 1, 2, 1)
        self.assertEqual(rope.tail_is_touching_head(), True)

    def test_tail_is_touching_head__touching_diag__true(self):
        rope = Rope(1, 1, 2, 2)
        self.assertEqual(rope.tail_is_touching_head(), True)

if __name__ == '__main__':
    unittest.main()