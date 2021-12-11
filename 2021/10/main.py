LINES = [line.strip() for line in open("input").readlines()]

POINTS_MAP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

P2_POINTS_MAP = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

OPENING = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


def corrupted_score(line):
    prev = []
    for c in line:
        if c not in OPENING:
            prev.append(c)
        elif prev.pop() != OPENING[c]:
            return POINTS_MAP[c]
    return 0


def p1():
    return sum(map(corrupted_score, LINES))


def complete(line):
    prev = []
    for c in line:
        if c not in OPENING:
            prev.append(c)
        elif prev[-1] == OPENING[c]:
            prev.pop()

    sm = 0
    for p in prev[::-1]:
        sm = sm * 5 + P2_POINTS_MAP[p]

    return sm


def p2():
    incomplete = filter(lambda x: corrupted_score(x) == 0, LINES)
    return (c := sorted(map(complete, incomplete)))[len(c) // 2]


print("1:", p1())
print("2:", p2())
