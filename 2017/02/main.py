rows = [list(map(int, row.strip().split())) for row in open("input", "r").readlines()]


def p1(row: list) -> int:
    return max(row) - min(row)


def p2(row: list) -> int:
    for n in row:
        for m in row:
            if n == m:
                continue
            if n % m == 0:
                return n // m


print("1:", sum(map(p1, rows)))
print("2:", sum(map(p2, rows)))
