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

    def test_parse_instruction__with_argument__opocode_parsed_correctly(self):
        instruction = parse_instruction("addx -5")
        self.assertEqual(instruction.opcode, "addx")

    def test_parse_instruction__with_argument__arg_parsed_correctly(self):
        instruction = parse_instruction("addx -5")
        self.assertEqual(instruction.arg, -5)

    def test_parse_instruction__no_argument__opcode_parsed_correctly(self):
        instruction = parse_instruction("noop")
        self.assertEqual(instruction.opcode, "noop")

    def test_parse_instruction__no_argument__arg_parsed_correctly(self):
        instruction = parse_instruction("noop")
        self.assertEqual(instruction.arg, None)

    def test_cpu_run__x_register_correct(self):
        call_stack = parse_instructions("test_input_basic.txt")
        cpu = CPU(call_stack)
        cpu.run()
        self.assertEqual(cpu.x, -1)

    def test_cpu_add_signal_strength(self):
        call_stack = parse_instructions("test_input.txt")
        watch_list = 20, 60, 100, 140, 180, 220
        cpu = CPU(call_stack, watch_list)
        cpu.run()
        self.assertEqual(cpu.total_signal_strength, 13140)

if __name__ == '__main__':
    unittest.main()