import unittest
from stack import Stack
from main import Day5

class Day5Tests(unittest.TestCase):
    def test_parse_stacks__stack_count(self):
        solver = Day5(True)
        
        solver.parse_stacks()
        stack_count = len(solver._stacks)

        self.assertEqual(stack_count, 3)

    def test_parse_stacks__crate_stack1(self):
        solver = Day5(True)
        
        solver.parse_stacks()
        expected = ['Z', 'N']
        actual = solver._stacks[0]._stack

        self.assertListEqual(expected, actual)

    def test_parse_instructions__count(self):
        solver = Day5(True)
        
        solver.parse_instructions()
        expected = 4
        actual = len(solver._instructions)

        self.assertEqual(expected, actual)

    def test_stack_multi_push(self):
        stack = Stack([])
        stack.multi_push([1,2,3])
        expected = [1,2,3]
        actual = stack._stack

        self.assertEqual(expected, actual)  

    def test_stack_multi_pop_popped(self):
        stack = Stack([1, 2, 3, 4, 5])
        actual = stack.multi_pop(2)
        expected = [4,5]

        self.assertEqual(expected, actual)  

    def test_stack_multi_pop_stack(self):
        stack = Stack([1, 2, 3, 4, 5])
        stack.multi_pop(2)
        expected = [1,2,3]
        actual = stack._stack

        self.assertEqual(expected, actual)  

    def test_full(self):
        solver = Day5(True)
        
        actual = solver.solve()
        expected = "MCD"

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()