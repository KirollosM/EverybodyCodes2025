def cycle(x1, y1, x2, y2):
    new1 = x1 * x1 - y1 * y1
    new2 = 2 * x1 * y1

    new1 //= 10
    new2 //= 10

    new1 += x2
    new2 += y2

    return new1, new2


A1, A2 = 166, 52
R1, R2 = 0, 0

for _ in range(3):
    R1, R2 = cycle(R1, R2, A1, A2)

print(R1, R2)
