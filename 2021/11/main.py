GRID = [[int(l) for l in line.strip()] for line in open("input").readlines()]

ROWS = len(GRID)
COLS = len(GRID[0])


def neighbours(x, y):
    return [(dx, dy) for dx in range(x-1, x+2) for dy in range(y-1, y+2) if (dx, dy) != (x, y) and 0 <= dx < COLS and 0 <= dy < ROWS]


def simulate():
    flashes = 0

    to_flash = []

    for y in range(ROWS):
        for x in range(COLS):
            GRID[y][x] += 1
            if GRID[y][x] > 9:
                to_flash.append((x, y))

    while len(to_flash) > 0:
        x, y = to_flash.pop(0)
        if GRID[y][x] > 9:
            GRID[y][x] = 0
            flashes += 1
            for dx, dy in neighbours(x, y):
                if GRID[dy][dx] == 0:
                    continue
                GRID[dy][dx] += 1
                if GRID[dy][dx] > 9:
                    to_flash.append((dx, dy))

    return flashes


def p1():
    sm = 0
    for _ in range(100):
        sm += simulate()
    return sm


def p2():
    # Skip first 100 iterations bc destructive GRID
    ctr = 101
    while simulate() != 100:
        ctr += 1
    return ctr


print("1:", p1())
print("2:", p2())
