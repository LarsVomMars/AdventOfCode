LINES = [int(line.strip()) for line in open("input").readlines()]


def p1():
    return sum([a < b for a, b in zip(LINES, LINES[1:])])


def p2():
    return sum([sum(LINES[i:i+3]) < sum(LINES[i+1:i+1+3]) for i in range(0, len(LINES) - 2)])


print("1:", p1())
print("2:", p2())
