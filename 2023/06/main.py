import re

reg_nums = re.compile(r"\d+")

time_str, dist_str = open("input").readlines()
TIME = list(map(int, reg_nums.findall(time_str)))
DIST = list(map(int, reg_nums.findall(dist_str)))

TOTAL_TIME = int(reg_nums.findall(time_str.replace(" ", ""))[0])
TOTAL_DIST = int(reg_nums.findall(dist_str.replace(" ", ""))[0])


def get_range(time, dist):
    return [res for i in range(0, time + 1) if (res := i * (time - i)) > dist]


def p1():
    res = 1
    for t, d in zip(TIME, DIST):
        res *= len(get_range(t, d))
    return res


def p2():
    return len(get_range(TOTAL_TIME, TOTAL_DIST))


print("1:", p1())
print("2:", p2())
