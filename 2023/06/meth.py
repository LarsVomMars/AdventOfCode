import re
from math import sqrt, floor, ceil

reg_nums = re.compile(r"\d+")

time_str, dist_str = open("input").readlines()
TIME = list(map(int, reg_nums.findall(time_str)))
DIST = list(map(int, reg_nums.findall(dist_str)))

TOTAL_TIME = int(reg_nums.findall(time_str.replace(" ", ""))[0])
TOTAL_DIST = int(reg_nums.findall(dist_str.replace(" ", ""))[0])


def calc_diff(time, dist):
    a = time / 2
    b = (-a) ** 2 - dist
    return ceil(a + sqrt(b)) - floor(a - sqrt(b)) - 1


def p1():
    res = 1
    for t, d in zip(TIME, DIST):
        res *= calc_diff(t, d)
    return res


def p2():
    return calc_diff(TOTAL_TIME, TOTAL_DIST)


print("1:", p1())
print("2:", p2())
