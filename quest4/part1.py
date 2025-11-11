with open("part1.txt", "r") as f:
    teeth = []
    for l in f:
        teeth.append(int(l))


ratio = 1

count = 0

while count < len(teeth) - 1:
    ratio *= teeth[count] / teeth[count + 1]
    count += 1

print(ratio * 2025)
