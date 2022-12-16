import re


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


FILE = open("input").read()
REG = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

# Don't ask
DATA = list(map(lambda x: ((int(x[0]), int(x[1])), dist(
    (int(x[0]), int(x[1])), (int(x[2]), int(x[3])))), REG.findall(FILE)))


def ranges(s, d, y):
    """
    Just use start and end of the range
    """
    sy = d - abs(y - s[1])
    if sy > 0:
        return s[0] - sy, s[0] + sy
    return []


def check(c11, c12, c21, c22):
    """
    Fast edge (line segment) intersection check using meth
    https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    Im not gonna pretend that i fully understand this
    """
    x1, y1 = c11
    x2, y2 = c12
    x3, y3 = c21
    x4, y4 = c22

    nom = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
    den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if den == 0:
        return -1, -1
    
    res = nom / den
    x = int(x1 + res * (x2 - x1))
    y = int(y1 + res * (y2 - y1))
    return x, y


def p1():
    fields = []
    y = int(2e6)
    for s, d in DATA:
        fields.extend(ranges(s, d, y))
    return max(fields) - min(fields)


def p2():
    bound = int(4e6)
    polys = [
        # clockwise corners of the diamond
        (
            (s[0] + (d+1), s[1]),
            (s[0], s[1] + (d+1)),
            (s[0] - (d+1), s[1]),
            (s[0], s[1] - (d+1)),
        ) for s, d in DATA
    ]
    
    for d, d1 in enumerate(polys):
        for d2 in polys[d+1:]:
            # Check every edge against every edge
            for i in range(4):
                for j in range(4):
                    x, y = check(d1[i], d1[(i+1) % 4], d2[j], d2[(j+1) % 4])
                    if 0 <= x <= bound and 0 <= y <= bound and all(dist((x, y), s) > d for s, d in DATA):
                        return x * 4000000 + y
    return -1


print("1:", p1())
print("2:", p2())
