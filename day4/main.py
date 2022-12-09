def parse_input(file_name):
    pairs = []
    with open(file_name) as f:
        lines = f.read().splitlines()
        for line in lines:
            # split into assignments
            assignments = line.split(",")
            # split elves into lower and upper bounds
            ass1 = assignments[0].split("-")
            ass2 = assignments[1].split("-")

            pairs.append(((int(ass1[0]), int(ass1[1])), (int(ass2[0]), int(ass2[1]))))
    return pairs

def is_containment(assignment1, assignment2):
    lower1 = assignment1[0]
    upper1 = assignment1[1]
    lower2 = assignment2[0]
    upper2 = assignment2[1]
    return (lower1 >= lower2 and upper1 <= upper2) or (lower1 <= lower2 and upper1 >= upper2)
    
def is_overlap(assignment1, assignment2):
    lower1 = assignment1[0]
    upper1 = assignment1[1]
    lower2 = assignment2[0]
    upper2 = assignment2[1]
    return not (upper1 < lower2 or upper2 < lower1)

def solve(file_name, condition):
    pairs = parse_input(file_name)
    containment_count = 0
    for pair in pairs:
        if condition(pair[0], pair[1]):
            containment_count += 1
    return containment_count

file = "input.txt"
print("PART 1:", solve(file, is_containment))
print("PART 2:", solve(file, is_overlap))