rows = open("input", "r").readlines()
rows = [row.strip().split() for row in rows]

def test(instructions: list):
    visited = []
    A = 0
    i = 0
    while True:
        if i in visited:
            return [False, A]
        if i >= len(instructions):
            return [True, A]

        visited.append(i)
        row = instructions[i]
        if row[0] == "jmp":
            i += int(row[1])
        elif row[0] == "nop":
            i += 1
        elif row[0] == "acc":
            A += int(row[1])
            i += 1

i = 0
while True:
    if rows[i][0] == "jmp":
        rows[i][0] = "nop"
    elif rows[i][0] == "nop":
        rows[i][0] = "jmp"

    if not rows[i][0] == "acc":
        res = test(rows)
        if res[0]:
            print(res)
            break

    f = open("input", "r")
    rows = open("input", "r").readlines()
    rows = [row.strip().split() for row in rows]
    i += 1


        