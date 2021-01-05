rows = open("input", "r").readlines()

rows = [row.strip().split() for row in rows]
visited = []

A = 0
i = 0
while True:
    if i in visited:
        print(A)
        break

    visited.append(i)
    row = rows[i]
    if row[0] == "jmp":
        i += int(row[1])
    elif row[0] == "nop":
        i += 1
    elif row[0] == "acc":
        A += int(row[1])
        i += 1
