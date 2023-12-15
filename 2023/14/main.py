GRID = [line.strip() for line in open("input").readlines()]


def rotate(lines):
    grid = []
    for i in range(len(lines[0])):
        grid.append("".join([line[i] for line in lines[::-1]]))
    return grid


def tilt(lines):
    grid = []
    for line in lines:
        parts = line.split("#")
        parts = ["".join(sorted(part)) for part in parts]
        grid.append("#".join(parts))
    return grid


def rt(lines):
    return rotate(tilt(lines))


def score(lines):
    sm = 0
    for line in lines:
        for s, char in enumerate(line, 1):
            if char == "O":
                sm += s
    return sm


GRID = rotate(GRID)


def p1(grid):
    new_grid = tilt(grid)
    return score(new_grid)


def p2(grid):
    current = grid
    seen = list()
    cycles = 0
    while True:
        for _ in range(4):
            current = rt(current)
        if current in seen:
            break
        seen.append(current)
        cycles += 1
    cycle_index = seen.index(current)
    cycle_length = cycles - cycle_index
    idx = cycle_index + ((1000000000 - cycle_index - 1) % cycle_length)
    return score(seen[idx])


print("1:", p1(GRID))
print("2:", p2(GRID))
