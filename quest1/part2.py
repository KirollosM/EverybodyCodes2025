with open("part2.txt", "r") as r:
    names = r.readline().split(",")
    r.readline()
    moves = r.readline().split(",")

index = 0

for move in moves:
    multiplier = 1 if move[0] == "R" else -1
    counter = int(move[1:])

    index = ((counter * multiplier) + index) % (len(names))

print(names[index])
