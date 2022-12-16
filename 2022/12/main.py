from networkx import DiGraph, shortest_path_length, has_path
from math import inf


def mp(x):
    nx = ord(x) - 97
    if nx == -14:
        return 0
    elif nx == -28:
        return 25
    return nx


FILE = open("input").read()
GRID = [list(map(mp, list(line.strip()))) for line in FILE.splitlines()]

GRAPH = DiGraph()

data = FILE.replace("\n", "")
s = data.index("S")
START = (s % len(GRID[0]), s // len(GRID[0]))
e = data.index("E")
END = (e % len(GRID[0]), e // len(GRID[0]))


def get_adjacent(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(GRID[0]) and 0 <= ny < len(GRID):
            yield nx, ny


for y, row in enumerate(GRID):
    for x, col in enumerate(row):
        for nx, ny in get_adjacent(x, y):
            if GRID[ny][nx] <= GRID[y][x] + 1:
                GRAPH.add_edge((x, y), (nx, ny))


def path(start, end):
    if not has_path(GRAPH, start, end):
        return inf
    return shortest_path_length(GRAPH, start, end)


def p1():
    return path(START, END)


def p2():
    dist = inf
    for y, row in enumerate(GRID):
        for x, col in enumerate(row):
            if col == 0:
                new_dist = path((x, y), END)
                dist = min(dist, new_dist)  # type: ignore
    return dist


print("1:", p1())
print("2:", p2())
