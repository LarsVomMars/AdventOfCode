import re

REG = re.compile(r"(\d+)")
LINES = [
    list(map(int, REG.findall(line.strip()))) for line in open("input").readlines()
]


def p1():
    sm = 0
    for s, *e in LINES:
        c = [e[0]]
        for x in e[1:]:
            nc = []
            for y in c:
                nc.append(x + y)
                nc.append(x * y)
            c = nc
        if s in c:
            sm += s
    return sm


def p2():
    sm = 0
    for s, *e in LINES:
        c = [e[0]]
        for x in e[1:]:
            nc = []
            for y in c:
                nc.append(x + y)
                nc.append(x * y)
                nc.append(int(str(y) + str(x)))
            c = nc
        if s in c:
            sm += s
    return sm


print("1:", p1())
print("2:", p2())
