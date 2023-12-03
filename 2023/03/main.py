from collections import defaultdict

LINES = [line.strip() for line in open("input").readlines()]

numbers = dict()
symbols = dict()

for y, row in enumerate(LINES):
    current = ""
    index = (0, 0)
    for x, char in enumerate(row):
        if not char.isdigit():
            if current:
                numbers[index] = current
                current = ""
            if char != ".":
                index = (y, x)
                symbols[index] = char
            continue

        if char.isdigit():
            if not current:
                index = (y, x)
            current += char
            continue
    if current:
        numbers[index] = current


def all():
    gears = defaultdict(list)

    p1 = 0
    p2 = 0

    for key in numbers:
        value = numbers[key]
        start = (key[0] - 1, key[1] - 1)
        end = (key[0] + 1, key[1] + len(value))
        adjacent = list(
            filter(
                lambda x: x[0] >= start[0]
                and x[0] <= end[0]
                and x[1] >= start[1]
                and x[1] <= end[1],
                symbols.keys(),
            )
        )
        
        if len(adjacent) == 0:
            continue
        
        val = int(value)
        for f in filter(lambda k: symbols[k] == "*", adjacent):
            gears[f].append(val)
        p1 += val

    for key in gears:
        value = gears[key]
        if len(value) == 2:
            p2 += value[0] * value[1]

    return p1, p2


p1, p2 = all()

print("1:", p1)
print("2:", p2)
