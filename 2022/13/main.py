from json import loads
from functools import cmp_to_key

LINES = [[loads(l.strip()) for l in line.splitlines()]
         for line in open("input").read().split("\n\n")]

LINES2 = [loads(line.strip()) for line in open(
    "input").read().splitlines() if line.strip() != '']


def compare_list(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        return l1 - l2
    elif isinstance(l1, list) and isinstance(l2, list):
        i = 0
        while i < len(l1) and i < len(l2):
            c = compare_list(l1[i], l2[i])
            if c != 0:
                return c
            i += 1
        return len(l1) - len(l2)
    elif isinstance(l1, int) and isinstance(l2, list):
        return compare_list([l1], l2)
    elif isinstance(l1, list) and isinstance(l2, int):
        return compare_list(l1, [l2])


def p1():
    cnt = 0
    for i, lst in enumerate(LINES):
        l1, l2 = lst
        res = compare_list(l1, l2)
        if res < 0:  # type: ignore
            cnt += i + 1
    return cnt


def p2():
    sorted_lines = sorted(
        LINES2 + [[[2]], [[6]]], key=cmp_to_key(lambda l1, l2: compare_list(l1, l2)))  # type: ignore
    return (sorted_lines.index([[2]]) + 1) * (sorted_lines.index([[6]]) + 1)


print("1:", p1())
print("2:", p2())
