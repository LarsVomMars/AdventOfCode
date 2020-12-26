rows = open("input", "r").readlines()
rows = [row.strip() for row in rows]

ADJ = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

prev = []
ctr = 0
while prev != rows:
    prev = rows.copy()
    urows = rows.copy()
    for i in range(len(rows)):  # row
        for j in range(len(rows[i])):  # col
            row = list(urows[i])
            if rows[i][j] == ".":
                continue
            oc = 0
            for pos in ADJ:
                b = False
                f = 1
                while True:
                    if i + f * pos[0] < 0 or i + f * pos[0] >= len(rows) or j + f * pos[1] < 0 or j + f * pos[1] >= len(row):
                        break
                    if rows[i + f * pos[0]][j + f * pos[1]] == "#":
                        b = True
                        break
                    elif rows[i + f * pos[0]][j + f * pos[1]] == "L":
                        break
                    f += 1
                oc += 1 if b else 0
            if oc >= 5 and rows[i][j] == "#":
                row[j] = "L"
            elif oc == 0 and rows[i][j] == "L":
                row[j] = "#"
            urows[i] = "".join(row)
    ctr += 1
    rows = urows.copy()

print("".join(rows).count("#"))
