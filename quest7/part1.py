with open("part1.txt", "r") as f:
    lines = f.readlines()

    names = lines[0].split(",")

    rules = dict()

    for line in lines[2 : len(lines)]:
        pre, post = line.split(">")

        rules[pre.strip()] = post.strip().split(",")


total = 0
for name in names:
    flag = True

    count = 0
    while count < len(name) - 1:
        if not (name[count + 1] in rules[name[count]]):
            flag = False
            break

        count += 1

    if flag:
        total += 1
        print(name)

print(total)
