import unittest
from main import *
from crt import CRT
from cpu import CPU
from instruction import Instruction

class DayTenTests(unittest.TestCase):
    def test_crt_tick__empty_stack__exception_raised(self):
        crt = CRT()
        self.assertRaises(Exception, crt.tick)

    def test_crt_run__addx__takes_two_cpu_cycles(self):
        stack = [Instruction("addx", 3)]
        crt = CRT(stack)
        crt.run()
        self.assertEqual(crt.cpu.cycle, 3)

    # INFINITE LOOP!
    # def test_get_total_signal_strength(self):
    #     actual = get_total_signal_strength("test_input.txt")
    #     expected = 13140
    #     self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()