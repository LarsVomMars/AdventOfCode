import re


def parse(a, b, c, d):
    return (set(range(a, b+1)), set(range(c, d+1)))


FILE = open('input').read()
REG = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

DATA = list(map(lambda x: parse(*list(map(int, x))), REG.findall(FILE)))


def p1():
    return sum(map(lambda x: x[0] >= x[1] or x[0] <= x[1], DATA))


def p2():
    return sum(map(lambda x: len(x[0] & x[1]) > 0, DATA))


print("1:", p1())
print("2:", p2())
