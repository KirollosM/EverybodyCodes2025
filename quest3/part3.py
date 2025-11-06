from collections import Counter

with open("part3.txt", "r") as f:
    nums = [int(x) for x in f.readline().split(",")]


freq = Counter(nums)

print(max(freq.values()))
