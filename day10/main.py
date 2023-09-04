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

# sprite is 3 pixels wide
# x register is middle of sprite
# Screen draws single pixel during each cpu cycle
# screen produces # if sprite is visible or . if not

# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240

# print out resulting image (this is what I should get from the example)

##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....

# timing will be tricky here: distinction between DURING cycle and AFTER cycle important
# sprite pixels drawin during cycle; result of opcode occurs after cycle
# TODO : Watch Racing the Beam