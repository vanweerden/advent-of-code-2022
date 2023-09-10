from instruction import Instruction
from crt import CRT
from cpu import CPU

def parse_instruction(line):
    split = line.split(" ")
    opcode = split[0]
    arg = int(split[1]) if len(split) > 1 else None
    return Instruction(opcode, arg)

def get_instructions(file_name):
    with open(file_name) as f:
        instructions = []
        for line in f.read().splitlines():
            instructions.append(parse_instruction(line))
        return instructions

def get_call_stack(file_name):
    stack = get_instructions(file_name)
    stack.reverse()
    return stack

# PART 1 Methods
def get_total_signal_strength(file_name):
    call_stack = get_call_stack(file_name)
    crt = CRT(call_stack)
    crt.run()
    return crt.total_signal_strength

def solve_part_1():
    print("PART 1")
    print(get_total_signal_strength("input.txt"))

def solve_part_2(file_name):
    call_stack = get_call_stack(file_name)
    crt = CRT(call_stack)
    crt.run()


solve_part_2("input.txt")