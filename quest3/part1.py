with open("part1.txt", "r") as f:
    nums = [int(x) for x in f.readline().split(",")]

nums = set(nums)
nums = list(nums)

print(sum(sorted(nums, reverse=True)))
