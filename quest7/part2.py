with open("part2.txt", "r") as f:
    lines = f.readlines()

    names = lines[0].split(",")

    rules = dict()

    for line in lines[2 : len(lines)]:
        pre, post = line.split(">")

        rules[pre.strip()] = post.strip().split(",")


total = 0
for idx in range(len(names)):
    name = names[idx]
    flag = True

    count = 0
    while count < len(name) - 2:
        if not (name[count + 1] in rules.get(name[count], [])):
            flag = False
            break

        count += 1

    if flag:
        total += idx + 1
        print(name)

print(total)
