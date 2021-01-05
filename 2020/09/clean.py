rows = list(map(int, open("input", "r").readlines()))

num = None

for i, row in enumerate(rows[25:]):
    preamble = rows[i:i + 26]
    b = False
    for p in preamble:
        for o in preamble:
            if o + p == row and not o == p:
                b = True
                break
        if b:
            break

    if not b:
        print("1:", num := row)
        break

for i in range(len(rows)):
    j = i
    s = 0
    while True:
        s += rows[j]
        if s >= num:
            break
        j += 1

    if s == num:
        r = rows[i:j + 1]
        print("2:", min(r) + max(r))
        break
