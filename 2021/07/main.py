from math import inf, ceil, floor
from statistics import mean, median

DATA = [int(num) for num in open("input").read().split(",")]


def p1():
    m = int(median(DATA))
    return sum([abs(m - num) for num in DATA])


def gauss(n): return n * (n + 1) // 2


def p2():
    mi = min(DATA)
    ma = max(DATA)
    least_fuel = inf
    for i in range(mi, ma + 1):
        fuel = sum([gauss(abs(i - num)) for num in DATA])
        least_fuel = min(fuel, least_fuel)

    mn = mean(DATA)
    umn = ceil(mn)
    lmn = floor(mn)

    return (
        least_fuel,
        sum([gauss(abs(umn - num)) for num in DATA]),
        sum([gauss(abs(lmn - num)) for num in DATA])
    )


print("1:", p1())
print("2:", p2())
