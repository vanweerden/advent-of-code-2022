from instruction import Instruction

class CPU:
    debug = False

    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.current_instruction = None
        self.instruction_cycles_left = 0

        self.opcode_duration = {
            "noop": 1, 
            "addx": 2
        }

        self.valid_opcodes = ["noop", "addx"]
        self.total_signal_strength = 0

    def load_instruction(self, instruction):
        self.throw_exception_if_invalid(instruction)
        self.current_instruction = instruction
        self.instruction_cycles_left = self.opcode_duration[instruction.opcode]

        if self.debug:
            print(f'Begin executing {instruction.opcode} {instruction.arg}')

    def begin_cycle(self):
        self.cycle += 1

        if self.debug:
            print(f'[CPU] Start cycle {self.cycle} (x: {self.x})')

        self.instruction_cycles_left -= 1

    def finish_cycle(self):
        if self.debug:
            print(f'[CPU] Cycle {self.cycle} finished (x: {self.x})')
        if self.instruction_cycles_left == 0:
            self.execute()

    def execute(self):
        if self.debug:
            print(f'[CPU] Executing {self.current_instruction.opcode}')
            
        if self.current_instruction.opcode == "addx":
            v = self.current_instruction.arg
            self.addx(v)
        self.current_instruction = None

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