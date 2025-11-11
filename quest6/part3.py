from collections import Counter

with open("part3.txt", "r") as f:
    base = f.read().strip()

letters = base * 1000
summer = 0

count = Counter()

l = 0
r = 0
for i in range(len(letters)):
    l = max(0, i - 1000)
    r = min(len(letters) - 1, i + 1000)

    ch = letters[i]
    if ch.islower():
        summer += letters[l : r + 1].count(ch.upper())

print(summer)
