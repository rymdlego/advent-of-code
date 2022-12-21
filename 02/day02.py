PART1 = {
    "A X": 4,  # rock vs rock          = draw
    "B X": 1,  # paper vs rock         = lose
    "C X": 7,  # scissors vs rock      = win
    "A Y": 8,  # rock vs paper         = win
    "B Y": 5,  # paper vs paper        = draw
    "C Y": 2,  # scissors vs paper     = lose
    "A Z": 3,  # rock vs scissors      = lose
    "B Z": 9,  # paper vs scissors     = win
    "C Z": 6,  # scissors vs scissors  = draw
}

PART2 = {
    "A X": 3,  # lose against rock     = scissors
    "B X": 1,  # lose against paper    = rock
    "C X": 2,  # lose against scissors = paper
    "A Y": 4,  # draw against rock     = rock
    "B Y": 5,  # draw against paper    = paper
    "C Y": 6,  # draw against scissors = scissors
    "A Z": 8,  # win against rock      = paper
    "B Z": 9,  # win against paper     = scissors
    "C Z": 7,  # win against scissors  = rock
}

with open("input", "r") as f:
   input = f.read().strip()

rounds = input.split("\n")

print(f"Part A: {sum(PART1[round] for round in rounds)}")
print(f"Part B: {sum(PART2[round] for round in rounds)}")
