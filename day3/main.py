def parse_input(file):
    with open(file_name) as f:
        return f.read().splitlines()

def parse_input_grouped(file, collection_size):
    groups = []
    with open(file_name) as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), collection_size):
            group = lines[i:i+collection_size]
            groups.append(group)
    return groups

def find_dup_char_in_two(s1, s2):
    for c in s1:
        if c in s2:
            return c
    raise Exception("No duplicate items found")

def find_dup_char_in_three(s1, s2, s3):
    for c in s1:
        if c in s2 and c in s3:
            return c
    raise Exception("No duplicate items found")


def priority_of(char):
    ascii_val = ord(char)

    if ascii_val >= 65 and ascii_val <= 90:
        return ascii_val-38
    elif ascii_val >= 97 and ascii_val <= 122:
        return ascii_val-96
    else:
        raise Exception(f"{char} is not a letter")

def solve_part_1(file):
    priority_sum = 0
    rucksacks = parse_input(file)
    for rucksack in rucksacks:
        compart_size = int(len(rucksack)/2)
        compartment_1 = rucksack[:compart_size]
        compartment_2 = rucksack[compart_size:]
        priority_sum += priority_of(find_dup_char_in_two(compartment_1, compartment_2))
    return priority_sum

def solve_part_2(file):
    priority_sum = 0
    group_size = 3
    groups = parse_input_grouped(file, group_size)

    for g in groups:
        badge = find_dup_char_in_three(g[0], g[1], g[2])
        priority_sum += priority_of(badge)
    return priority_sum

# PART 1: Find total priority value of dupe items 
file_name = "input.txt"
print("PART 1:", solve_part_1(file_name))

# PART 2: Find the item type that corresponds to the badges of each three-Elf group and calc total priority
print("PART 2:", solve_part_2(file_name))
