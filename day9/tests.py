import sys
import unittest
from main import *
from rope import Rope

class DayNineTests(unittest.TestCase):
    file = "test_input.txt"

    # def test_tail_is_touching_head__not_touching_hor__false(self):
    #     rope = Rope(1, 1, 1, 3)
    #     self.assertEqual(rope.tail_is_touching_head(), False)

    # def test_tail_is_touching_head__not_touching_vert__false(self):
    #     rope = Rope(1, 1, 3, 1)
    #     self.assertEqual(rope.tail_is_touching_head(), False)

    # def test_tail_is_touching_head__not_touching_diag__false(self):
    #     rope = Rope(1, 1, 2, 3)
    #     self.assertEqual(rope.tail_is_touching_head(), False)

    # def test_tail_is_touching_head__touching_hor__true(self):
    #     rope = Rope(1, 1, 1, 2)
    #     self.assertEqual(rope.tail_is_touching_head(), True)

    # def test_tail_is_touching_head__touching_vert__true(self):
    #     rope = Rope(1, 1, 2, 1)
    #     self.assertEqual(rope.tail_is_touching_head(), True)

    # def test_tail_is_touching_head__touching_diag__true(self):
    #     rope = Rope(1, 1, 2, 2)
    #     self.assertEqual(rope.tail_is_touching_head(), True)

    # UPDATE TAIL: HORIZONTAL MOVES
    def test__update_tail_pos__hor_move_right__tail_moves_right(self):
        #.T.H. -> ..TH.
        head_row = 1
        head_col = 3
        tail_row = 1
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, 1)
        self.assertEqual(rope.tail_col, 2)

    def test__update_tail_pos__hor_move_left__tail_moves_left(self):
        #.H.T. -> ..HT.
        head_row = 1
        head_col = 1
        tail_row = 1
        tail_col = 3
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, 1)
        self.assertEqual(rope.tail_col, 2)

    def test__update_tail_pos__tail_adjacent__no_move(self):
         #..HT. -> ..HT.
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 3
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    # # UPDATE TAIL: VERTICAL MOVES
    def test__update_tail_pos__vert_move_up__tail_moves_up(self):
        # .     .
        # H ->  H
        # .     T
        # T     .
        head_row = 1
        head_col = 1
        tail_row = 3
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, head_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, 2)
        self.assertEqual(rope.tail_col, tail_col)

    # def test__update_tail_pos__vert_move_down__tail_moves_down(self):
        # .     .
        # T ->  .
        # .     T
        # H     H
        head_row = 3
        head_col = 1
        tail_row = 1
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, 2)
        self.assertEqual(rope.tail_col, tail_col)

    def test__update_tail_pos__tail_vert_adjacent__no_move(self):
        # .     .
        # T ->  T
        # H     H
        # .     .
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    def test__update_tail_pos__on_top__no_move(self):
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 2
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    # # UPDATE TAIL: DIAGONAL
    # def test__update_tail_pos__bottom_left_row_span__moves_below(self):
    #     # .....     .....
    #     # ..H..     ..H..
    #     # ..... ->  ..T..
    #     # .T...     .....
    #     head_row = 1
    #     head_col = 2
    #     tail_row = 3
    #     tail_col = 1
    #     rope = Rope(head_row, head_col, tail_row, tail_col)

    #     rope.update_tail_pos()

    #     self.assertEqual(rope.tail_row, 2)
    #     self.assertEqual(rope.tail_col, 2)

    # def test__update_tail_pos__bottom_left_col_span__moves_to_left(self):
    #     # ....     ....
    #     # ..H.     .TH.
    #     # T... ->  ....
    #     # ....     ....
    #     head_row = 1
    #     head_col = 2
    #     tail_row = 2
    #     tail_col = 0
    #     rope = Rope(head_row, head_col, tail_row, tail_col)

    #     rope.update_tail_pos()

    #     self.assertEqual(rope.tail_row, 1)
    #     self.assertEqual(rope.tail_col, 1)

    # def test__update_tail_pos__diagonal_adjacent__no_move(self):
    #     # ....     ....
    #     # ..H.     ..H.
    #     # .T.. ->  .T..
    #     # ....     ....
    #     head_row = 1
    #     head_col = 2
    #     tail_row = 2
    #     tail_col = 1
    #     rope = Rope(head_row, head_col, tail_row, tail_col)

    #     rope.update_tail_pos()

    #     self.assertEqual(rope.tail_row, tail_row)
    #     self.assertEqual(rope.tail_col, tail_col)

    # MOVE HEAD


if __name__ == '__main__':
    unittest.main()