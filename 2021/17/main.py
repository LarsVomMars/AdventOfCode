import re
from dataclasses import dataclass
from pydantic import validate_arguments
from math import isqrt


@validate_arguments
@dataclass
class TargetRange:
    xmin: int
    xmax: int
    ymin: int
    ymax: int

    def has(self, x, y):
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax


line = open("input").read().strip()

TARGET = TargetRange(
    *re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", line).groups())


def p1():
    # I have no clue why this works
    return -TARGET.ymin * (-TARGET.ymin - 1) // 2


def sign(x):
    return 1 if x > 0 else 0 if x == 0 else -1


def run(vx, vy):
    cx = 0
    cy = 0

    while True:
        cx += vx
        cy += vy
        if cy < TARGET.ymin or cx > TARGET.xmax:
            return False

        if TARGET.has(cx, cy):
            return True

        vx -= sign(vx)
        vy -= 1


def p2():
    return sum(
        run(vx, vy)
        for vx in range(isqrt(TARGET.xmin), TARGET.xmax + 1)
        for vy in range(TARGET.ymin, abs(TARGET.ymin) + 1)
    )


print("1:", p1())
print("2:", p2())
