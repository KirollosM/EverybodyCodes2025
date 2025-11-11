with open("part3.txt", "r") as f:
    l = []
    r = f.read().split("\n")
    for i in r:
        j = i.split("|")
        for k in j:
            if k:
                l.append(int(k))

ratio = 1

for i in range(0, len(l), 2):
    ratio *= l[i] / l[i + 1]

print(ratio * 100)
