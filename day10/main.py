from instruction import Instruction
from cpu import CPU

def parse_instruction(line):
    split = line.split(" ")
    opcode = split[0]
    arg = int(split[1]) if len(split) > 1 else None
    return Instruction(opcode, arg)

def parse_instructions(file_name):
    # TODO: Reverse the list of instructions so first instructions is popped of first (like a real stack)

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

# Refactor!
# Create CRT class that contains CPU and CRT classes
# CRT class has look that ticks
# On each tick, it calls CPU.tick(), which updates its cycle etc.
# CRT class feeds instructions to CPU (or maybe CPU should contain call stack)
# Move methods that solve part 1 to CRT
# Solve part 1

# sprite is 3 pixels wide
# x register is middle of sprite
# Screen draws single pixel during each cpu cycle, from left-to-right
# If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.). 
# SO need to track
# 1: sprite position
# 2: which pixel is being drawn (this is the cycle number)
# for each cycle, need to determine whether any of the three pixels is positioned at index (cycle no.)

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
