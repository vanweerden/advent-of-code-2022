from instruction import Instruction

class CPU:
    def __init__(self,  watch_list=[], verbose=False):
        self.cycle = 0
        self.x = 1
        self.current_instruction = None
        self.instruction_cycles_left = 0

        self.opcode_duration = {
            "noop": 1,
            "addx": 2
        }

        self._verbose_mode = verbose
        self.valid_opcodes = ["noop", "addx"]
        self.watch_list = sorted(watch_list)
        self.total_signal_strength = 0

    def tick(self):
        if self.instruction_cycles_left > 0:
            self.instruction_cycles_left -= 1
        else:
            self.execute()
    
    def begin_execution(self, instruction):
        # Begin an instruction    
        self.throw_exception_if_invalid(instruction)
        self.current_instruction = instruction
        self.instruction_cycles_left = self.opcode_duration[instruction.opcode]

    def execute(self):
        if self.current_instruction.opcode == "addx":
            v = self.current_instruction.arg
            self.addx(v)


        self.cycle+=1
        if (self._verbose_mode):
            print(f'[DEBUG] Cycle: { self.cycle }, x: { self.x }')
        if (self.is_watched_cycle()):
            self.add_signal_strength()

    def addx(self, v):
        self.x+=v

    def is_valid_opcode(self, opcode):
        return opcode in self.valid_opcodes

    def throw_exception_if_invalid(self, instruction):
        if (not isinstance(instruction, Instruction)):
             raise Exception(f"Expected Instruction but received {type(instruction)}")
        elif(not instruction.opcode in self.valid_opcodes):
             raise Exception(f"Unknown opcode '{instruction.opcode}'")
        elif(instruction.arg != None and not isinstance(instruction.arg, int)):
             raise Exception(f"Argument should be int, not {type(instruction.arg)}")
        
    def is_watched_cycle(self):
        return self.cycle in self.watch_list

    def add_signal_strength(self):
        self.total_signal_strength += self.calculate_signal_strength()

    def calculate_signal_strength(self):
        return self.cycle * self.x
