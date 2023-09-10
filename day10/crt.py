from cpu import CPU

class CRT:
    debug = False
    # PART 1
    watch_list = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0

    # PART 2
    lit_pixel = "#"
    dark_pixel = "."
    screen_width = 40

    def __init__(self, call_stack=[]):
        self.call_stack = call_stack
        self.cpu = CPU()

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
        if (self.cpu.cycle in self.watch_list):
            self.add_signal_strength()

        self.print_pixel()

        self.cpu.finish_cycle()

    def print_pixel(self):
        if self.sprite_is_over_pixel():
            print(self.lit_pixel, end="")
        else:
            print(self.dark_pixel, end="")

        if self.cpu.cycle % self.screen_width == 0:
            print("")

    # PART 1 methods
    def add_signal_strength(self):
        signal_strength = self.calculate_signal_strength()
        self.total_signal_strength += signal_strength
    def calculate_signal_strength(self):
        return self.cpu.cycle * self.cpu.x

    def sprite_is_over_pixel(self):
        current_pixel = (self.cpu.cycle-1) % self.screen_width
        return current_pixel in range(self.cpu.x-1, self.cpu.x+2)