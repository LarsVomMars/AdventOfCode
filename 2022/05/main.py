import re
from copy import deepcopy

rows, moves = open("input").read().split("\n\n")
rows = re.sub(r"[\[\]]", " ", rows)
*rows, _ = rows.split("\n")
idxs = [i for i, c in enumerate(rows[-1]) if c.isalpha()]
COLS = [[] for _ in idxs]

for i, idx in enumerate(idxs):
    for row in rows:
        if row[idx] == " ":
            continue
        COLS[i] += [row[idx]]

for i, col in enumerate(COLS):
    COLS[i] = list(reversed(col))


REG = re.compile(r"move (\d+) from (\d+) to (\d+)")
MOVES = list(map(lambda x: list(map(int, x)), REG.findall(moves)))


def p1(cols):
    for c, f, t in MOVES:
        for _ in range(c):
            cols[t - 1].append(cols[f - 1].pop())
    return "".join([col[-1] for col in cols])


def p2(cols):
    for c, f, t in MOVES:
        tm = cols[f - 1][-c:]
        cols[f - 1] = cols[f - 1][:-c]
        cols[t - 1] += tm
    return "".join([col[-1] for col in cols])


print("1:", p1(deepcopy(COLS)))
print("2:", p2(deepcopy(COLS)))
