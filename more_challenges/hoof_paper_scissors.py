games = input()
moves = []

for i in range(int(games)):
    moves.append(input())

for move in moves:
    if move == "hoof":
        print("paper")
        continue
    elif move == "paper":
        print("scissors")
        continue
    elif move == "scissors":
        print("hoof")
        continue
