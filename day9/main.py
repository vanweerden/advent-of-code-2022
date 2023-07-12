"""
Another Matrix problem!
TODO: Write tests for update_tail_pos using examples
    x hor
    x vert
    x on top
    x diagonal
TODO: Write tests for move_head and get them to pass
    - R 4
    - U 4
    - L 3
    - D 1
    - R 4
    - D 1
    - L 5
    - R 2
TODO: Get tests to pass

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