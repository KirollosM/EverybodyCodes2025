top_left = (-79785, 15616)


def add(n1, n2, x, y):
    return (n1 + x, n2 + y)


bottom_right = add(top_left[0], top_left[1], 1000, 1000)


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def div_trunc(a, b):
    return (a[0] // b[0], a[1] // b[1])


def engrave(x, y):
    R = 0, 0
    for i in range(100):
        R = mul(R, R)
        R = div_trunc(R, (100000, 100000))
        R = add(R[0], R[1], x, y)

        if abs(R[0]) > 1000000 or abs(R[1]) > 1000000:
            return False

    return True


step = 1
base_x = top_left[0]
base_y = top_left[1]
count = 0

for dy in range(0, 1001, step):
    y = base_y + dy
    for dx in range(0, 1001, step):
        x = base_x + dx
        if engrave(x, y):
            count += 1

print(count)
