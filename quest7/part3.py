with open("part3.txt", "r") as f:
    lines = f.readlines()

    names = [name.strip() for name in lines[0].split(",")]

    rules = dict()

    for line in lines[2 : len(lines)]:
        pre, post = line.split(">")

        rules[pre.strip()] = [r.strip() for r in post.strip().split(",")]


unique_names = set()


def dfs(n):
    if 7 <= len(n) <= 11:
        unique_names.add(n)
    if len(n) == 11:
        return
    for nxt in rules.get(n[-1], []):
        dfs(n + nxt)


for name in names:
    count = 0
    flag = True
    while count < len(name) - 1:
        if not (name[count + 1] in rules.get(name[count], [])):
            flag = False
            break

        count += 1

    if 7 <= len(name) <= 11 and flag:
        unique_names.add(name)
    if flag:
        dfs(name)

print(len(unique_names))
