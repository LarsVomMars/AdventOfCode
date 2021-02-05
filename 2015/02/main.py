rows = [row.strip() for row in open("input", "r").readlines()]


def p1(row: str) -> int:
    sides = sorted(list(map(int, row.split("x"))))
    area = 2 * sides[0] * sides[1] + 2 * sides[1] * sides[2] + 2 * sides[0] * sides[2]
    slack = sides[0] * sides[1]
    return area + slack


def p2(row: str) -> int:
    sides = sorted(list(map(int, row.split("x"))))
    per = 2 * sides[0] + 2 * sides[1]
    bow = sides[0] * sides[1] * sides[2]
    return per + bow


print("1:", sum(map(p1, rows)))
print("2:", sum(map(p2, rows)))
