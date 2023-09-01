import unittest
from main import *
from cpu import CPU
from instruction import Instruction

class DayTenTests(unittest.TestCase):
    def test_noop__takes_one_cycle(self):
        cpu = CPU()
        instruction = Instruction("noop")
        cpu.execute(instruction)
        self.assertEqual(cpu.cycle, 1)

    def test_noop__x_stays_same(self):
        cpu = CPU()
        instruction = Instruction("noop")
        cpu.execute(instruction)
        self.assertEqual(cpu.x, 1)

    def test_addx__takes_two_cycles(self):
        cpu = CPU()
        instruction = Instruction("addx", 3)
        cpu.execute(instruction)
        self.assertEqual(cpu.cycle, 2)

    def test_addx__x_increments(self):
        cpu = CPU()
        instruction = Instruction("addx", 3)
        cpu.execute(instruction)
        self.assertEqual(cpu.x, 4)

    def test_throw_exception_if_invalid__invalid_instruction__exception_raised(self):
        cpu = CPU()
        invalid_instruction = 3
        self.assertRaises(Exception, cpu.execute, invalid_instruction)

    def test_throw_exception_if_invalid__invalid_opcode__exception_raised(self):
        cpu = CPU()
        invalid_instruction = Instruction("foo", 3)
        self.assertRaises(Exception, cpu.execute, invalid_instruction)

    def test_throw_exception_if_invalid__invalid_opcode_arg__exception_raised(self):
        cpu = CPU()
        invalid_instruction = Instruction("addx", "foo")
        self.assertRaises(Exception, cpu.execute, invalid_instruction)

if __name__ == '__main__':
    unittest.main()