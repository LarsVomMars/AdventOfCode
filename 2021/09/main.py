GRID = [[int(n) for n in line.strip()] for line in open("input").readlines()]

ROWS = len(GRID)
COLS = len(GRID[0])


def get_neighbours(x, y):
    # CW Neighbors
    nbs = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    for col, row in nbs:
        if 0 <= col < COLS and 0 <= row < ROWS:
            yield col, row


def p1():
    return sum(GRID[row][col] + 1 for row in range(ROWS) for col in range(COLS)
               if all(GRID[row][col] < GRID[y][x] for x, y in get_neighbours(col, row)))


def bs(x, y, checked):
    if (x, y) in checked or GRID[y][x] == 9:
        return -1

    checked.add((x, y))
    to_check = [(x, y)]
    size = 0

    while len(to_check) > 0:
        pos = to_check.pop()
        size += 1

        for nb in get_neighbours(*pos):
            if nb not in checked and GRID[nb[1]][nb[0]] != 9:
                to_check.append(nb)
                checked.add(nb)

    return size


def p2():
    checked = set()
    sizes = sorted([bs(x, y, checked) for x in range(COLS)
                    for y in range(ROWS)])[::-1]
    return sizes[0] * sizes[1] * sizes[2]


print("1:", p1())
print("2:", p2())
