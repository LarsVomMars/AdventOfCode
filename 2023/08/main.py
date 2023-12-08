import re
from math import lcm

INSTRUCTIONS, paths = open("input").read().split("\n\n")
INSTRUCTIONS = list(map(int, INSTRUCTIONS.replace("L", "0").replace("R", "1")))

MAPS = dict()

REG = re.compile(r"((\w+) = \((\w+)\, (\w+)\))")

for _, start, left, right in REG.findall(paths):
    MAPS[start] = (left, right)


def walk(start):
    steps = 0
    current = start
    while current[-1] != "Z":
        current = MAPS[current][INSTRUCTIONS[steps % len(INSTRUCTIONS)]]
        steps += 1
    return steps


def p1():
    return walk("AAA")


def p2():
    return lcm(*[walk(k) for k in MAPS.keys() if k[-1] == "A"])


print("1:", p1())
print("2:", p2())
