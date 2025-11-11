from collections import Counter

with open("part2.txt", "r") as f:
    letters = f.read()


count = Counter()

total = 0
for ch in letters:
    if not ch.islower():
        count[ch] += 1
    else:
        total += count[ch.upper()]

print(total)
