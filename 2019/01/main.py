masses = [int(row.strip()) for row in open("input", "r").readlines()]


def p1(mass: int) -> int:
    res = mass // 3 - 2
    return res if res >= 0 else 0


def p2(mass: int) -> int:
    fuel = 0
    res = p1(mass)
    while not res == 0:
        fuel += res
        res = p1(res)
    return fuel


print("1:", sum(map(p1, masses)))
print("2:", sum(map(p2, masses)))
