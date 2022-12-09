class Stack:
    def __init__(self, stack=[]):
        self._stack = stack

    def push(self, item):
        self._stack.append(item)

    def multi_push(self, items):
        for item in items:
            self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def multi_pop(self, n):
        start_index = len(self._stack)-n
        rtn = self._stack[start_index:]
        self._stack = self._stack[:start_index]
        return rtn

    def peek(self):
        stack_len = len(self._stack)
        if stack_len > 0:
            return self._stack[stack_len-1]
        else:
            return ""

    def count(self):
        return len(self._stack)
