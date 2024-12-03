LINES = list(
    zip(*[map(int, line.strip().split()) for line in open("input").readlines()])
)

C1 = LINES[0]
C2 = LINES[1]


def p1():
    return sum([abs(e1 - e2) for e1, e2 in zip(sorted(C1), sorted(C2))])


def p2():
    return sum([C2.count(i) * i for i in C1])


print("1:", p1())
print("2:", p2())
