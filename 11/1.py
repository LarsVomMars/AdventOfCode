rows = open("input", "r").readlines()
rows = [row.strip() for row in rows]

prev = []

sour = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

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
            for pos in sour:
                if i+pos[0] < 0 or i+pos[0] >= len(rows) or j+pos[1] < 0 or j+pos[1] >= len(row):
                    continue
                oc += 1 if rows[i+pos[0]][j+pos[1]] == "#" else 0
            if oc >= 4 and rows[i][j] == "#":
                row[j] = "L"
            elif oc == 0 and rows[i][j] == "L":
                row[j] = "#"
            urows[i] = "".join(row)
    ctr += 1
    rows = urows.copy()

print("".join(rows).count("#"))
