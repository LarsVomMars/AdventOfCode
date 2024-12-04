from itertools import product

LINES = [line.strip() for line in open("input").readlines()]
ROWS = len(LINES)
COLS = len(LINES[0])

XMAS = "XMAS"


def check(x, y, dx, dy):
    for i in range(1, 4):
        x += dx
        y += dy
        if not (0 <= x < COLS) or not (0 <= y < ROWS) or LINES[y][x] != XMAS[i]:
            return False
    return True


DIRS = set(product(range(-1, 2), repeat=2)) - {(0, 0)}


def p1():
    return sum(
        [
            LINES[y][x] == "X" and check(x, y, dx, dy)
            for y in range(ROWS)
            for x in range(COLS)
            for dx, dy in DIRS
        ]
    )


def diag(x, y):
    tl = LINES[y - 1][x - 1]
    tr = LINES[y - 1][x + 1]
    bl = LINES[y + 1][x - 1]
    br = LINES[y + 1][x + 1]

    return (
        tl == "M" and br == "S" and tr == "M" and bl == "S"
        or tl == "M" and br == "S" and tr == "S" and bl == "M"
        or tl == "S" and br == "M" and tr == "M" and bl == "S"
        or tl == "S" and br == "M" and tr == "S" and bl == "M"
    )


def p2():
    return sum(
        [
            LINES[y][x] == "A" and diag(x, y)
            for y in range(1, ROWS - 1)
            for x in range(1, COLS - 1)
        ]
    )


print("1:", p1())
print("2:", p2())
