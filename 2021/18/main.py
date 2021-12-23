from json import loads
from math import ceil
from functools import reduce
from itertools import permutations


LINES = [loads(line) for line in open("input").readlines()]


def magnitude(value):
    if isinstance(value, list):
        return 3 * magnitude(value[0]) + 2 * magnitude(value[1])
    elif isinstance(value, int):
        return value
    else:
        raise Exception("Invalid type")


def split(value):
    if isinstance(value, int):
        if value >= 10:
            return [value // 2, ceil(value / 2)]
        return None

    new_val = split(value[0])
    if new_val is not None:
        return [new_val, value[1]]

    new_val = split(value[1])
    if new_val is not None:
        return [value[0], new_val]

    return None


def left_add(list, value):
    if isinstance(list, int):
        return list + value
    return [left_add(list[0], value), list[1]]


def right_add(list, value):
    if isinstance(list, int):
        return list + value
    return [list[0], right_add(list[1], value)]


def explode(value, depth=0):
    if isinstance(value, int):
        return 0, None, 0
    if depth == 4:
        return value[0], 0, value[1]

    left, new_val, right = explode(value[0], depth + 1)
    if new_val is not None:
        return left, [new_val, left_add(value[1], right)], 0

    left, new_val, right = explode(value[1], depth + 1)
    if new_val is not None:
        return 0, [right_add(value[0], left), new_val], right

    return 0, None, 0


def add(base, value):
    new_list = [base, value]

    while True:
        _, res, _ = explode(new_list)
        if res is not None:
            new_list = res
            continue

        res = split(new_list)
        if res is not None:
            new_list = res
            continue

        return new_list


def p1():
    return magnitude(reduce(add, LINES))


def p2():
    return max(magnitude(reduce(add, perm)) for perm in permutations(LINES, 2))


print("1:", p1())
print("2:", p2())
