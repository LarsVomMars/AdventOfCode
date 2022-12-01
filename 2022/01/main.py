ELVES = sorted(map(sum, [[int(line.strip()) for line in row.split("\n")
                          if line.strip() != ''] for row in open("input").read().split("\n\n")]))


def p1():
    return ELVES[-1]


def p2():
    return sum(ELVES[-3:])


print("1:", p1())
print("2:", p2())
