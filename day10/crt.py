from cpu import CPU

class CRT:
    def __init__(self, call_stack=[]):
        self.call_stack = call_stack
        self.cpu = CPU()
        self.screen_width = 40

        self.watch_list = [20, 60, 100, 140, 180, 220]
        self.total_signal_strength = 0
        self.debug = False

    def run(self):
        self.cpu.load_instruction(self.call_stack.pop())

        while len(self.call_stack) > 0 or self.cpu.current_instruction != None:
            if self.cpu.current_instruction == None:
                self.cpu.load_instruction(self.call_stack.pop())

            # start next cycle
            self.tick()

    def tick(self):
        self.cpu.begin_cycle()

        # "During" cycle
        if (self.is_watched_cycle()):
            self.add_signal_strength()

        self.cpu.finish_cycle()


    # PART 1 methods
    def is_watched_cycle(self):
        return self.cpu.cycle in self.watch_list
    def add_signal_strength(self):
        signal_strength = self.calculate_signal_strength()
        self.total_signal_strength += signal_strength
    def calculate_signal_strength(self):
        return self.cpu.cycle * self.cpu.x