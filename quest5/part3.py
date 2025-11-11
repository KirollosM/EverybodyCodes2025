qualities = []

with open("part3.txt", "r") as f:
    for line in f.readlines():

        id, nums = line.split(":")
        id = int(id)
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

        tiers = [
            int("".join("" if num is None else str(num) for num in seg))
            for seg in layers
        ]
        qualities.append((int(quality), tiers, id))

qualities.sort(reverse=True)
ids = [sword[2] for sword in qualities]

print(sum((id * index for index, id in enumerate(ids, start=1))))
