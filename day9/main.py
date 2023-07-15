"""

Main:
1) Feed all directions to rope
2) Each time head moves on step, update tail position
3) Mark positions that Tail visits on each iteration
4) Count the number of positions the tail has visited at least once

CLASSES
- Rope 
    * METHOD: update tail position given head position
    * METHOD: move head given instruction and update tail position after each step
- Matrix to mark which positions tail has visited (simple mark as True)
"""

file = "input.txt"
def solve_part_1(input):
    
