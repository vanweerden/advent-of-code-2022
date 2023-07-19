import sys
import unittest
from main import *
from rope import Rope

class DayNineTests(unittest.TestCase):
    file = "test_input.txt"

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

    # UPDATE TAIL: DIAGONAL
    def test__update_tail_pos__bottom_left__moves_below(self):
        # .....     .....
        # ..H..     ..H..
        # ..... ->  ..T..
        # .T...     .....
        head_row = 1
        head_col = 2
        tail_row = 3
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row+1)
        self.assertEqual(rope.tail_col, head_col)

    def test__update_tail_pos__bottom_right__moves_below(self):
        # .....     .....
        # ..H..     ..H..
        # ..... ->  ..T..
        # ...T.     .....
        head_row = 1
        head_col = 2
        tail_row = 3
        tail_col = 3
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row+1)
        self.assertEqual(rope.tail_col, head_col)

    def test__update_tail_pos__left_bottom__moves_to_left(self):
        # ....     ....
        # ..H.     .TH.
        # T... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 0
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row)
        self.assertEqual(rope.tail_col, head_col-1)

    def test__update_tail_pos__left_top__moves_to_left(self):
        # ....     ....
        # T...     ....
        # ..H. ->  .TH.
        # ....     ....
        head_row = 2
        head_col = 2
        tail_row = 1
        tail_col = 0
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row)
        self.assertEqual(rope.tail_col, head_col-1)

    def test__update_tail_pos__top_left__moves_above(self):
        # T...     ....
        # ....     .T..
        # .H.. ->  .H..
        # ....     ....
        head_row = 2
        head_col = 1
        tail_row = 0
        tail_col = 0
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row-1)
        self.assertEqual(rope.tail_col, head_col)

    def test__update_tail_pos__top_right__moves_above(self):
        # ..T.     ....
        # ....     .T..
        # .H.. ->  .H..
        # ....     ....
        head_row = 2
        head_col = 1
        tail_row = 0
        tail_col = 2
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row-1)
        self.assertEqual(rope.tail_col, head_col)

    def test__update_tail_pos__right_top__moves_to_right(self):
        # ....     ....
        # ..T.     ....
        # H... ->  HT..
        # ....     ....
        head_row = 2
        head_col = 0
        tail_row = 1
        tail_col = 2
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row)
        self.assertEqual(rope.tail_col, head_col+1)

    def test__update_tail_pos__right_lower__moves_to_right(self):
        # ....     ....
        # ....     ....
        # H... ->  HT..
        # ..T.     ....
        head_row = 2
        head_col = 0
        tail_row = 3
        tail_col = 2
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, head_row)
        self.assertEqual(rope.tail_col, head_col+1)

    def test__update_tail_pos__diagonal_adjacent_1__no_move(self):
        # ....     ....
        # ..H.     ..H.
        # .T.. ->  .T..
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    def test__update_tail_pos__diagonal_adjacent_2__no_move(self):
        # .T..     .T..
        # ..H.     ..H.
        # .... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 0
        tail_col = 1
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    def test__update_tail_pos__diagonal_adjacent_3__no_move(self):
        # ...T     ...T
        # ..H.     ..H.
        # .... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 0
        tail_col = 3
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    def test__update_tail_pos__diagonal_adjacent_4__no_move(self):
        # ....     ....
        # ..H.     ..H.
        # ...T ->  ...T
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 3
        rope = Rope(head_row, head_col, tail_row, tail_col)

        rope.update_tail_pos()

        self.assertEqual(rope.tail_row, tail_row)
        self.assertEqual(rope.tail_col, tail_col)

    def test_count_tail_positions(self):
        actual = count_tail_positions(self.file)
        expected = 15

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()