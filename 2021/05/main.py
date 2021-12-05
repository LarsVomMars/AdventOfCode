import re
from collections import defaultdict

DATA = open("input").read()
creg = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
COORDS = list(map(lambda x: list(map(int, x)), creg.findall(DATA)))


def p1():
    grid = defaultdict(int)
    for x1, y1, x2, y2 in COORDS:
        if x1 == x2:
            yup = y1 < y2
            for y in range(y1, y2 + 1 if yup else y2 - 1, 1 if yup else -1):
                grid[x1, y] += 1
        elif y1 == y2:
            xup = x1 <= x2
            for x in range(x1, x2 + 1 if xup else x2 - 1, 1 if xup else -1):
                grid[x, y1] += 1

    return sum(grid[x, y] > 1 for x, y in grid.keys())


def p2():
    grid = defaultdict(int)
    for x1, y1, x2, y2 in COORDS:
        if x1 == x2:
            yup = y1 < y2
            for y in range(y1, y2 + 1 if yup else y2 - 1, 1 if yup else -1):
                grid[x1, y] += 1
        elif y1 == y2:
            xup = x1 <= x2
            for x in range(x1, x2 + 1 if xup else x2 - 1, 1 if xup else -1):
                grid[x, y1] += 1
        else:
            xup = x1 <= x2
            yup = y1 <= y2
            for x, y in zip(range(x1, x2 + 1 if xup else x2 - 1, 1 if xup else -1),
                            range(y1, y2 + 1 if yup else y2 - 1, 1 if yup else -1)):
                grid[x, y] += 1

    return sum(grid[x, y] > 1 for x, y in grid.keys())


print("1:", p1())
print("2:", p2())
