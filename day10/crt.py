from cpu import CPU

class CRT:
    def __init__(self, call_stack=[]):
        self.call_stack = call_stack
        self.cpu = CPU()

    def tick(self):
        if (len(self.call_stack) == 0):
            raise Exception("No instructions found in stack")
        self.cpu.tick()

    def run(self):
        while len(self.call_stack) > 0:
            if self.cpu.current_instruction == None:
                next_operation = self.call_stack.pop()
            self.cpu.begin_execution(next_operation)
            self.cpu.tick()


    # TODO: add methods for solving part 1 here