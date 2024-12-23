import re

INPUT = open("input").read()

REG = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))")


def all():
    p1 = 0
    p2 = 0
    enabled = True
    for match, a, b in REG.findall(INPUT):
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        else:
            p1 += int(a) * int(b)
            p2 += int(a) * int(b) * enabled

    return p1, p2


p1, p2 = all()
print("1:", p1)
print("2:", p2)
