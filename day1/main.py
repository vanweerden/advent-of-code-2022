# parse lines
file_name = "input.txt"
raw_data = []
with open(file_name) as f:
    raw_data = f.read().splitlines()

# create empty list of total calories
calories_per_elf = []

# add numbers in lines
accumulator = 0
for n in raw_data:
    if len(n) > 0:
        accumulator += int(n)
    # when reach blank line, add total to list and reset total
    else:
        calories_per_elf.append(accumulator)
        accumulator = 0

# get largest number from list
max_calories = max(calories_per_elf)
print("max calories:", max_calories)

# get sum of top three
top_three = sorted(calories_per_elf, reverse = True)[:3]
print("sum of top three:", sum(top_three))