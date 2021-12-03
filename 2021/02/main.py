import re

file = open('input').read()
reg = re.compile(r'(\w+) (\d+)')

DATA = list(map(lambda x: (x[0], int(x[1])), reg.findall(file)))


def p1():
    pos = [0, 0]
    for dir, dist in DATA:
        if dir == 'forward':
            pos[0] += dist
        elif dir == 'down':
            pos[1] += dist
        elif dir == 'up':
            pos[1] -= dist
    return pos[0] * pos[1]


def p2():
    pos = [0, 0]
    aim = 0
    for dir, dist in DATA:
        if dir == 'forward':
            pos[0] += dist
            pos[1] += aim * dist
        elif dir == 'down':
            aim += dist
        elif dir == 'up':
            aim -= dist
    return pos[0] * pos[1]


print("1:", p1())
print("2:", p2())
