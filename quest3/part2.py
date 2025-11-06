with open("part2.txt", "r") as f:
    nums = [int(x) for x in f.readline().split(",")]

nums = set(nums)
nums = list(nums)

count = 0

nums.sort()

for i in range(20):
    count += nums[i]

print(count)
