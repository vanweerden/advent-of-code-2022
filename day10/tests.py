import unittest
from main import *
from crt import CRT
from instruction import Instruction

class DayTenTests(unittest.TestCase):
    basic_test_input = "test_input_basic.txt"
    test_input = "test_input.txt"

    # Test cycles and x register with basic input
    def test_crt_run__x_correct(self):
        call_stack = get_call_stack(self.basic_test_input)
        crt = CRT(call_stack)
        
        crt.run()

        self.assertEqual(crt.cpu.x, -1)

    def test_crt_run__cycle_correct(self):
        call_stack = get_call_stack(self.basic_test_input)
        crt = CRT(call_stack)
        
        crt.run()

        self.assertEqual(crt.cpu.cycle, 5)

    def test_get_total_signal_strength(self):
        actual = get_total_signal_strength(self.test_input)

        self.assertEqual(actual, 13140)

    # INFINITE LOOP!
    # def test_get_total_signal_strength(self):
    #     actual = get_total_signal_strength("test_input.txt")
    #     expected = 13140
    #     self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()