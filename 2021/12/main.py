from collections import defaultdict

LINES = [line.strip() for line in open("input").readlines()]

CAVES = defaultdict(list)
for line in LINES:
    start, end = line.split("-")
    CAVES[start].append(end)
    CAVES[end].append(start)


def pathing(doubled=False, visited=set(), current="start"):
    if current == "end":
        return 1
    if current in visited:
        if current == "start":
            return 0
        if current.islower():
            if doubled:
                return 0
            doubled = True

    return sum(pathing(doubled, visited | {current}, next) for next in CAVES[current])


def p1():
    return pathing(True)


def p2():
    return pathing()


print("1:", p1())
print("2:", p2())
