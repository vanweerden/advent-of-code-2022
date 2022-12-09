from scanner import Scanner

signal = ""
file = "input.txt"
with open(file) as f:
    signal = f.read().splitlines()[0]

scanner = Scanner(signal)
part1 = scanner.start_of_packet()
print(part1)

part2 = scanner.start_of_message()
print(part2)