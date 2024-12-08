from collections import defaultdict
from itertools import combinations

LINES = [line.strip() for line in open("input").readlines()]
NODES = defaultdict(list)

MAX_Y = len(LINES)
MAX_X = len(LINES[0])

for y, line in enumerate(LINES):
    for x, c in enumerate(line):
        if c != ".":
            NODES[c].append((y, x))


def p1():
    antinodes = set()
    for coords in NODES.values():
        for a, b in combinations(coords, 2):
            diff = (a[0] - b[0], a[1] - b[1])
            nn = (a[0] + diff[0], a[1] + diff[1])
            pn = (b[0] - diff[0], b[1] - diff[1])
            if 0 <= nn[0] < MAX_Y and 0 <= nn[1] < MAX_X:
                antinodes.add(nn)
            if 0 <= pn[0] < MAX_Y and 0 <= pn[1] < MAX_X:
                antinodes.add(pn)

    return len(antinodes)


def p2():
    antinodes = set()
    for coords in NODES.values():
        for a, b in combinations(coords, 2):
            diff = (a[0] - b[0], a[1] - b[1])
            while True:
                nn = (a[0] + diff[0], a[1] + diff[1])
                if 0 <= nn[0] < MAX_Y and 0 <= nn[1] < MAX_X:
                    antinodes.add(nn)
                else:
                    break
                a = nn
            
            while True:
                pn = (b[0] - diff[0], b[1] - diff[1])
                if 0 <= pn[0] < MAX_Y and 0 <= pn[1] < MAX_X:
                    antinodes.add(pn)
                else:
                    break
                b = pn
        if len(coords) > 2:
            antinodes |= set(coords)
    
    return len(antinodes)


print("1:", p1())
print("2:", p2())