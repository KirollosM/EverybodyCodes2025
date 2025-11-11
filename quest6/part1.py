from collections import Counter

with open("part1.txt", "r") as f:
    letters = f.read()


count = Counter()

total = 0
for ch in letters:
    if not ch.islower():
        count[ch] += 1
    elif ch == "a":
        total += count["A"]

print(total)
