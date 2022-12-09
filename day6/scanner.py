class Scanner:
    def __init__(self, signal):
        self._signal = signal

    def start_of_packet(self):
        return self.scan(4)

    def start_of_message(self):
        return self.scan(14)

    def scan(self, chunk_size):
        current = self._signal[:chunk_size]
        for i in range(0, len(self._signal)):
            current = self._signal[i:i+chunk_size]
            if self.is_marker(current):
                return i+chunk_size
        raise Exception("Signal marker not found")

    def is_marker(self, chunk):
        stack = []
        for char in chunk:
            if char in stack:
                return False
            stack.append(char)
        return True