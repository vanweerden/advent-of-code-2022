file_name = "input.txt"

rock = "rock"
paper = "paper"
scissors = "scissors"
win = "win"
draw = "draw"
loss = "loss"

translator = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}

response_to = {
    rock: {
        win: paper,
        draw: rock,
        loss: scissors
    },
    paper: {
        win: scissors,
        draw: paper,
        loss: rock
    },
    scissors: {
        win: rock,
        draw: scissors,
        loss: paper
    } 
}

points_for = {
    loss: 0,
    draw: 3,
    win: 6,
    rock: 1,
    paper: 2,
    scissors:3 
}


rounds = []
with open(file_name) as f:
    raw_data = f.read().splitlines()
    for line in raw_data:
        split_line = line.split(" ")
        round = {
            "first_move": split_line[0],
            "result": split_line[1]
        }
        rounds.append(round)

# calculate score
total_score = 0
for r in rounds:
    first_move = translator[r["first_move"]]
    for_result = result = translator[r["result"]]
    response = response_to[first_move][for_result]
    total_score += points_for[response] + points_for[result]
print(total_score)