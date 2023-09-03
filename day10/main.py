from instruction import Instruction
from cpu import CPU

def parse_instruction(line):
    split = line.split(" ")
    opcode = split[0]
    arg = int(split[1]) if len(split) > 1 else None
    return Instruction(opcode, arg)

def parse_instructions(file_name):
    with open(file_name) as f:
        instructions = []
        for line in f.read().splitlines():
            instructions.append(parse_instruction(line))
        return instructions

def solve_part_1():
    instructions = parse_instructions("input.txt")
    watch_list = 20, 60, 100, 140, 180, 220
    cpu = CPU(instructions, watch_list)
    cpu.run()
    return cpu.total_signal_strength

print("PART 1")
print(solve_part_1())