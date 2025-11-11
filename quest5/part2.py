qualities = []

with open("part2.txt", "r") as f:
    for line in f.readlines():

        _, nums = line.split(":")
        nums = [int(i) for i in nums.split(",")]

        layers = []
        for n in nums:
            if not layers:
                layers.append([None, nums[0], None])
                continue

            placed = False
            for seg in layers:
                m = seg[1]
                if n < m and seg[0] is None:
                    seg[0] = n
                    placed = True
                    break
                if n > m and seg[2] is None:
                    seg[2] = n
                    placed = True
                    break

            if not placed:
                layers.append([None, n, None])

        quality = ""
        for seg in layers:
            quality = quality + str(seg[1])

        qualities.append(int(quality))

    print(max(qualities) - min(qualities))
