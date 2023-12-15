from itertools import combinations

LINES = [line.strip() for line in open("input").readlines()]

NODES = list()

for y, line in enumerate(LINES):
    for x, char in enumerate(line):
        if char == "#":
            NODES.append((x, y))


def expand(scale):
    ys = set(range(max(y for _, y in NODES) + 1)) - set(y for _, y in NODES)
    xs = set(range(max(x for x, _ in NODES) + 1)) - set(x for x, _ in NODES)

    for x, y in NODES:
        dy = len(list(filter(lambda ny: ny < y, ys)))
        dx = len(list(filter(lambda nx: nx < x, xs)))
        yield (x + dx * (scale - 1), y + dy * (scale - 1))


def solve(scale):
    g = expand(scale)
    pairs = list(combinations(g, 2))
    dists = list(
        map(
            lambda pair: abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]),
            pairs,
        )
    )
    return sum(dists)


def p1():
    return solve(2)


def p2():
    return solve(1000000)


print("1:", p1())
print("2:", p2())
