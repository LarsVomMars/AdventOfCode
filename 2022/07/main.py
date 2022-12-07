LINES = [line.strip() for line in open("input").readlines()]

DIRS = {}

cwd = "/"
root = 0
DIRS[cwd] = root

for line in LINES:
    if line.startswith("$"):
        _, cmd, *args = line.split()
        if cmd == "cd":
            arg = args[0]
            if arg == "..":
                cwd = "/".join(cwd.split("/")[:-2]) + "/"
            elif arg == "/":
                cwd = "/"
            else:
                cwd += arg + "/"
                if cwd not in DIRS:
                    DIRS[cwd] = 0
    else:
        a, b = line.split()
        if a == "dir":
            continue
        size = int(a)
        name = b
        DIRS[cwd] += size


nr = {}
for k, v in DIRS.items():
    if k == "/":
        nr[k] = v
        continue

    parts = k.split("/")
    prev_part = "/"
    for part in parts[:-1]:
        np = prev_part + part + "/"
        if part == "":
            np = "/"
        if np in nr:
            nr[np] += v
        else:
            nr[np] = v
        prev_part = np


def p1():
    return sum(v for v in nr.values() if v <= 100000)


def p2():
    from math import inf
    res = inf

    free = 70000000 - nr["/"]
    to_free = 30000000 - free

    for v in nr.values():
        if v >= to_free:
            res = min(v, res)
    return res


print("1:", p1())
print("2:", p2())
