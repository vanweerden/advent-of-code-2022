class CPU:
    def __init__(self, verbose=False):
        self.cycle = 0
        self.x = 1
        self._verbose_mode = verbose

    # def execute(self):
    #     for instruction in self.instructions:
    #         self.interpret(instruction)

    def interpret(self, instruction):
        split = instruction.split(" ")
        opcode = split[0]
        
        if (opcode == "noop"):
            self.noop()
        elif (opcode == "addx"):
            v = int(split[1])
            self.addx(v)

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