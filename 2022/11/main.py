from functools import reduce
from dataclasses import dataclass
from typing import Callable
from copy import deepcopy
from operator import mul, add


@dataclass
class Monkey:
    items: list[int]
    op: Callable[[int], int]
    throw: Callable[[int], int]
    mod: int


# Welcome to parser hell
data = open("input").read().split("\n\n")
MONKEYS: list[Monkey] = []


def monkey_op(x, op, opnum):
    return op(x, opnum)


def monkey_op_self(x, op):
    return op(x, x)


def monkey_throw(x, mod, tm, fm):
    return tm if x % mod == 0 else fm


for monkey in data:
    monkey = monkey.splitlines()

    items = list(map(int, monkey[1][18:].split(",")))

    rop = mul if "*" in monkey[2] else add

    mod = int(monkey[3].split()[-1])

    tm = int(monkey[4].split()[-1])
    fm = int(monkey[5].split()[-1])

    # Fuck python late-binding
    # Use partials or default parameters
    # Default parameters are evaluated at function definition time
    opnum = monkey[2].split()[-1]
    if opnum.isnumeric():
        opnum = int(opnum)

        def op(x, op=rop, opnum=opnum):
            return op(x, opnum)
    else:
        def op(x, op=rop):
            return op(x, x)

    def throw(x, mod=mod, tm=tm, fm=fm):
        return tm if x % mod == 0 else fm

    MONKEYS.append(Monkey(items, op, throw, mod))


def solve(monkeys: list[Monkey], rounds: int, div: bool):
    activity_map = [0, ] * len(monkeys)
    lcm = reduce(mul, [m.mod for m in monkeys])
    for _ in range(rounds):
        for mi, monkey in enumerate(monkeys):
            activity_map[mi] += len(monkey.items)
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                score = monkey.op(item) % lcm
                if div:
                    score //= 3
                nm = monkey.throw(score)
                monkeys[nm].items.append(score)

    activity_map = sorted(activity_map)
    return activity_map[-1] * activity_map[-2]


print("1:", solve(deepcopy(MONKEYS), 20, True))
print("2:", solve(deepcopy(MONKEYS), 10000, False))
