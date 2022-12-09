from stack import Stack
import re

class Day5:
    def __init__(self, test=False):
        self._stacks = []
        self._instructions = []
        self._input = []

        file = "test_input.txt" if test else "input.txt"
        with open(file) as f:
            self._input = f.read().splitlines()

    def solve(self):
        self.parse_stacks()
        self.parse_instructions()
        self.rearrange()
        return self.get_top_layer()

    def parse_stacks(self):
        final_line = 0
        for i in range(0, len(self._input)):
            if self._input[i][:2] == " 1":
                final_line = i
                break

        final_digits = self._input[final_line].replace(" ", "")
        stack_count = int(final_digits[len(final_digits)-1])

        self._stacks = [Stack([]) for x in range(0, stack_count)]

        line_number = final_line
        for line_number in reversed(range(0, final_line)):
            stack_number = 0
            line = self._input[line_number]

            for i in range(1, len(line), 4):
                char = line[i]
                if re.match(r'\w', char):
                    self._stacks[stack_number].push(char)
                stack_number += 1
                
    def parse_instructions(self):
        for i in range(len(self._input)):
            if self._input[i][:4] == "move":
                split = re.split(r'\D+', self._input[i])

                instruction = {
                    "quantity": int(split[1]),
                    "from": int(split[2])-1,
                    "to": int(split[3])-1
                }

                self._instructions.append(instruction)

    def rearrange(self):
        for instruction in self._instructions:
            src = self._stacks[instruction["from"]]
            dest = self._stacks[instruction["to"]]
            chunk = src.multi_pop(instruction["quantity"])
            dest.multi_push(chunk)
    
    def get_top_layer(self):
        top_layer = ""
        for stack in self._stacks:
            top_layer += stack.peek() 
        return top_layer

solver = Day5()
print("PART 2:", solver.solve())