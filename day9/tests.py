import sys
import unittest
from main import *
from rope import Rope

class DayNineTests(unittest.TestCase):
    # PART 1 TESTS
    def test__update_tail_pos__hor_move_right__tail_moves_right(self):
        #.T.H. -> ..TH.
        head_row = 1
        head_col = 3
        tail_row = 1
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)
        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row)
        self.assertEqual(rope.get_tail()[1], head_col-1)

    def test__update_tail_pos__hor_move_left__tail_moves_left(self):
        #.H.T. -> ..HT.
        head_row = 1
        head_col = 1
        tail_row = 1
        tail_col = 3
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], 1)
        self.assertEqual(rope.get_tail()[1], 2)

    def test__update_tail_pos__tail_adjacent__no_move(self):
         #..HT. -> ..HT.
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 3
        rope = Rope(2)
        rope.set_head(head_row, head_col)
        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__vert_move_up__tail_moves_up(self):
        # .     .
        # H ->  H
        # .     T
        # T     .
        head_row = 1
        head_col = 1
        tail_row = 3
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)
        self.set_tail(rope, tail_row, tail_col)
        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], 2)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__vert_move_down__tail_moves_down(self):
        # .     .
        # T ->  .
        # .     T
        # H     H
        head_row = 3
        head_col = 1
        tail_row = 1
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], 2)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__tail_vert_adjacent__no_move(self):
        # .     .
        # T ->  T
        # H     H
        # .     .
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__on_top__no_move(self):
        head_row = 1
        head_col = 2
        tail_row = 1
        tail_col = 2
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__bottom_left__moves_below(self):
        # .....     .....
        # ..H..     ..H..
        # ..... ->  ..T..
        # .T...     .....
        head_row = 1
        head_col = 2
        tail_row = 3
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)
        self.set_tail(rope, tail_row, tail_col)
        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row+1)
        self.assertEqual(rope.get_tail()[1], head_col)

    def test__update_tail_pos__bottom_right__moves_below(self):
        # .....     .....
        # ..H..     ..H..
        # ..... ->  ..T..
        # ...T.     .....
        head_row = 1
        head_col = 2
        tail_row = 3
        tail_col = 3
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row+1)
        self.assertEqual(rope.get_tail()[1], head_col)

    def test__update_tail_pos__left_bottom__moves_to_left(self):
        # ....     ....
        # ..H.     .TH.
        # T... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 0
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row)
        self.assertEqual(rope.get_tail()[1], head_col-1)

    def test__update_tail_pos__left_top__moves_to_left(self):
        # ....     ....
        # T...     ....
        # ..H. ->  .TH.
        # ....     ....
        head_row = 2
        head_col = 2
        tail_row = 1
        tail_col = 0
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row)
        self.assertEqual(rope.get_tail()[1], head_col-1)

    def test__update_tail_pos__top_left__moves_above(self):
        # T...     ....
        # ....     .T..
        # .H.. ->  .H..
        # ....     ....
        head_row = 2
        head_col = 1
        tail_row = 0
        tail_col = 0
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row-1)
        self.assertEqual(rope.get_tail()[1], head_col)

    def test__update_tail_pos__top_right__moves_above(self):
        # ..T.     ....
        # ....     .T..
        # .H.. ->  .H..
        # ....     ....
        head_row = 2
        head_col = 1
        tail_row = 0
        tail_col = 2
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row-1)
        self.assertEqual(rope.get_tail()[1], head_col)

    def test__update_tail_pos__right_top__moves_to_right(self):
        # ....     ....
        # ..T.     ....
        # H... ->  HT..
        # ....     ....
        head_row = 2
        head_col = 0
        tail_row = 1
        tail_col = 2
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row)
        self.assertEqual(rope.get_tail()[1], head_col+1)

    def test__update_tail_pos__right_lower__moves_to_right(self):
        # ....     ....
        # ....     ....
        # H... ->  HT..
        # ..T.     ....
        head_row = 2
        head_col = 0
        tail_row = 3
        tail_col = 2
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], head_row)
        self.assertEqual(rope.get_tail()[1], head_col+1)

    def test__update_tail_pos__diagonal_adjacent_1__no_move(self):
        # ....     ....
        # ..H.     ..H.
        # .T.. ->  .T..
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__diagonal_adjacent_2__no_move(self):
        # .T..     .T..
        # ..H.     ..H.
        # .... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 0
        tail_col = 1
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__diagonal_adjacent_3__no_move(self):
        # ...T     ...T
        # ..H.     ..H.
        # .... ->  ....
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 0
        tail_col = 3
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def test__update_tail_pos__diagonal_adjacent_4__no_move(self):
        # ....     ....
        # ..H.     ..H.
        # ...T ->  ...T
        # ....     ....
        head_row = 1
        head_col = 2
        tail_row = 2
        tail_col = 3
        rope = Rope(2)
        rope.set_head(head_row, head_col)

        self.set_tail(rope, tail_row, tail_col)

        rope.update_pos(1)

        self.assertEqual(rope.get_tail()[0], tail_row)
        self.assertEqual(rope.get_tail()[1], tail_col)

    def set_head(self, rope, row, col):
        rope._knots[0][0] = row
        rope._knots[0][1] = col

    def set_tail(self, rope, row, col):
        rope._knots[len(rope._knots)-1][0] = row
        rope._knots[len(rope._knots)-1][1] = col

    # def test_count_tail_positions_part_1(self):
    #     self.assertEqual(count_tail_positions("test_input.txt", 2), 15)

    def test_count_tail_positions_part_2(self):
        self.assertEqual(count_tail_positions("test_input_2.txt", 10), 36)

if __name__ == '__main__':
    unittest.main()