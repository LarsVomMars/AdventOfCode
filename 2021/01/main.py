LINES = [int(line.strip()) for line in open("input").readlines()]


def p1():
    return sum([1 for i in range(0, len(LINES) - 1) if LINES[i] < LINES[i+1]])


def p2():
    return sum([1 for i in range(0, len(LINES) - 1) if sum(LINES[i:i+3]) < sum(LINES[i+1:i+1+3])])


print("1:", p1())
print("2:", p2())
