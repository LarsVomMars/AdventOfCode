from functools import cache


INPUT = list(map(int, open("input").read().strip().split()))


@cache
def simulate_stone(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return simulate_stone(1, blinks - 1)

    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        return simulate_stone(int(s[: l // 2]), blinks - 1) + simulate_stone(
            int(s[l // 2 :]), blinks - 1
        )

    return simulate_stone(stone * 2024, blinks - 1)


def p1():
    return sum(map(lambda x: simulate_stone(x, 25), INPUT))


def p2():
    return sum(map(lambda x: simulate_stone(x, 75), INPUT))


print("1:", p1())
print("2:", p2())
