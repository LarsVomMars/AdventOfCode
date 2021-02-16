rows = [row.strip().replace(" through ", ";").split() for row in open("input", "r").readlines()]

instructions = {}
for row in rows:
    g = tuple(map(lambda x: tuple(map(int, x.split(","))), row[-1].split(";")))
    if row[0] == "turn":
        instructions[g] = True if row[1] == "on" else False
    else:
        instructions[g] = "tgl"


def p1(instructions: dict) -> int:
    grid = [[False] * 1000] * 1000
    for gid in instructions:
        si, sj = gid[0]
        ei, ej = gid[1]
        state = instructions[gid]
        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                grid[i][j] = state if type(state) == bool else not grid[i][j]

    return sum(map(lambda x: x.count(True), grid))


print("1:", p1(instructions))
