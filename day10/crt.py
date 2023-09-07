from cpu import CPU

class CRT:
    def __init__(self, call_stack=[], watch_list=[]):
        self.call_stack = call_stack
        self.cpu = CPU()
        self.screen_width = 40

        self.watch_list = watch_list
        self.total_signal_strength = 0

    def run(self):
        print(f'[CRT] Booting up')
        self.cpu.current_instruction = self.call_stack.pop()
        # BUG: For some reason, this is only being executed once
        while len(self.call_stack) > 0 or self.cpu.current_instruction != None:
            # handle current cycle
            if (len(self.call_stack) == 0):
                raise Exception("[CPU]: No instructions found in stack")

            if self.cpu.current_instruction == None:
                next_operation = self.call_stack.pop()
                self.cpu.begin_execution(next_operation)

            # part 1
            if (self.is_watched_cycle()):
                self.add_signal_strength()

            # start next cycle
            self.tick()

    def tick(self):
        print(f'[CRT] Tick')
        self.cpu.tick()

    # PART 1 methods
    def is_watched_cycle(self):
        return self.cpu.cycle in self.watch_list
    def add_signal_strength(self):
        self.total_signal_strength += self.calculate_signal_strength()
    def calculate_signal_strength(self):
        return self.cpu.cycle * self.cpu.x