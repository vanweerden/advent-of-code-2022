from instruction import Instruction

class CPU:
    def __init__(self, verbose=False):
        self.cycle = 1
        self.x = 1
        self.current_instruction = None
        self.instruction_cycles_left = 0

        self.opcode_duration = {
            "noop": 1,
            "addx": 2
        }

        self._verbose_mode = verbose
        self.valid_opcodes = ["noop", "addx"]
        self.total_signal_strength = 0

    def begin_execution(self, instruction):
        # Begin an instruction    
        self.throw_exception_if_invalid(instruction)
        self.current_instruction = instruction
        self.instruction_cycles_left = self.opcode_duration[instruction.opcode]

    def tick(self):
        if self.instruction_cycles_left == 0:
            self.execute()
        else:
            self.instruction_cycles_left -= 1

    def execute(self):
        if self.current_instruction.opcode == "addx":
            v = self.current_instruction.arg
            self.addx(v)

        if (self._verbose_mode):
            print(f'[CPU] Cycle: { self.cycle }, x: { self.x }')

    def addx(self, v):
        self.x+=v

    def is_valid_opcode(self, opcode):
        return opcode in self.valid_opcodes

    def throw_exception_if_invalid(self, instruction):
        if (not isinstance(instruction, Instruction)):
             raise Exception(f"[CPU]: Expected Instruction but received {type(instruction)}")
        elif(not instruction.opcode in self.valid_opcodes):
             raise Exception(f"[CPU]: Unknown opcode '{instruction.opcode}'")
        elif(instruction.arg != None and not isinstance(instruction.arg, int)):
             raise Exception(f"[CPU]: Argument should be int, not {type(instruction.arg)}")