from cpu import CPU

class CRT:
    def __init__(self, call_stack=[], watch_list=[]):
        self.call_stack = call_stack
        self.cpu = CPU()
        self.screen_width = 40

        self.watch_list = watch_list
        self.total_signal_strength = 0

    def tick(self):
        if (len(self.call_stack) == 0):
            raise Exception("[CPU]: No instructions found in stack")
        self.cpu.tick()

    def run(self):
        while len(self.call_stack) > 0:
            # handle current cycle
            if self.cpu.current_instruction == None:
                next_operation = self.call_stack.pop()
            self.cpu.begin_execution(next_operation)

            # part 1
            if (self.is_watched_cycle()):
                self.add_signal_strength()

            # start next cycle
            self.cpu.tick()

    # PART 1 methods
    def is_watched_cycle(self):
        return self.cpu.cycle in self.watch_list
    def add_signal_strength(self):
        self.total_signal_strength += self.calculate_signal_strength()
    def calculate_signal_strength(self):
        return self.cpu.cycle * self.cpu.x