from instruction import Instruction

class CPU:
    def __init__(self, call_stack=[], verbose=False):
        self.cycle = 0
        self.x = 1
        self._verbose_mode = verbose
        self._call_stack = call_stack # list of instructions
        self.valid_opcodes = ["noop", "addx"]

    def run(self):
        for instruction in self._call_stack:
            self.execute(instruction)

    def execute(self, instruction):
        self.throw_exception_if_invalid(instruction)
        if (instruction.opcode == "noop"):
            self.noop()
        elif (instruction.opcode == "addx"):
            self.addx(instruction.arg)

    def addx(self, v):
        required_cycles = 2
        for _ in range(required_cycles):
            self.tick()
        self.x+=v

    def noop(self):
        self.tick()

    def tick(self):
        self.cycle+=1
        if (self._verbose_mode):
            print(f'[DEBUG] Cycle: { self.cycle }')
            print(f'[DEBUG] x: { self.x }')

    def throw_exception_if_invalid(self, instruction):
        if (not isinstance(instruction, Instruction)):
             raise Exception(f"Expected Instruction but received {type(instruction)}")
        elif(not instruction.opcode in self.valid_opcodes):
             raise Exception(f"Unknown opcode '{instruction.opcode}'")
        elif(instruction.arg != None and not isinstance(instruction.arg, int)):
             raise Exception(f"Argument should be int, not {type(instruction.arg)}")
        
    def is_valid_opcode(self, opcode):
        return opcode in self.valid_opcodes