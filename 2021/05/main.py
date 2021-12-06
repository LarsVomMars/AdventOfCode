import re
from collections import defaultdict

DATA = open("input").read()
creg = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
COORDS = list(map(lambda x: list(map(int, x)), creg.findall(DATA)))


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def p1():
    grid = defaultdict(int)
    for x1, y1, x2, y2 in COORDS:
        if x1 == x2:
            dy = sign(y2 - y1)
            for y in range(y1, y2 + dy, dy):
                grid[x1, y] += 1
        elif y1 == y2:
            dx = sign(x2 - x1)
            for x in range(x1, x2 + dx, dx):
                grid[x, y1] += 1

    return sum(v > 1 for v in grid.values())


def p2():
    grid = defaultdict(int)
    for x1, y1, x2, y2 in COORDS:
        if x1 == x2:
            dy = sign(y2 - y1)
            for y in range(y1, y2 + dy, dy):
                grid[x1, y] += 1
        elif y1 == y2:
            dx = sign(x2 - x1)
            for x in range(x1, x2 + dx, dx):
                grid[x, y1] += 1
        else:
            dx = sign(x2 - x1)
            dy = sign(y2 - y1)
            for x, y in zip(range(x1, x2 + dx, dx),
                            range(y1, y2 + dy, dy)):
                grid[x, y] += 1

    return sum(v > 1 for v in grid.values())


print("1:", p1())
print("2:", p2())
