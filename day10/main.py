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

