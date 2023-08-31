import unittest
from main import *
from cpu import CPU

class DayTenTests(unittest.TestCase):
    def test__noop__takes_one_cycle(self):
        cpu = CPU()
        cpu.noop()
        self.assertEqual(cpu.cycle, 1)

    def test__addx__takes_two_cycles(self):
        cpu = CPU()
        cpu.addx(3)
        self.assertEqual(cpu.cycle, 2)

    def test__noop__x_stays_same(self):
        cpu = CPU()
        cpu.noop()
        self.assertEqual(cpu.x, 1)

    def test__addx__x_increments(self):
        cpu = CPU()
        cpu.addx(3)
        self.assertEqual(cpu.x, 4)

if __name__ == '__main__':
    unittest.main()