rows = [row.strip() for row in open("input", "r").readlines()]
distinct_chars = [set(row) for row in rows]


def p1():
    tw = 0
    th = 0
    for string, chars in zip(rows, distinct_chars):
        tw += 1 if any([string.count(char) == 2 for char in chars]) else 0
        th += 1 if any([string.count(char) == 3 for char in chars]) else 0
    return tw * th


def p2():
    for si, start in enumerate(rows):
        for running in rows[si:]:  # speed
            diff = 0
            didx = -1
            for ci, (sc, rc) in enumerate(zip(start, running)):
                if sc != rc:
                    diff += 1
                    didx = ci
            if diff == 1:
                s = list(start)
                del s[didx]
                return "".join(s)


print("1:", p1())
print("2:", p2())
