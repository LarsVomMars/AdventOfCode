LINES = [list(map(int, line.strip().split())) for line in open("input").readlines()]


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def p1():
    ctr = 0
    for line in LINES:
        dir = sign(line[1] - line[0])
        for a, b in zip(line, line[1:]):
            diff = b - a
            if 1 <= abs(diff) <= 3 and sign(diff) == dir:
                dir = sign(diff)
                continue
            break
        else:
            ctr += 1
    return ctr


# def tp2():
#     ctr = 0
#     solved = []
#     for line in LINES:
#         dir = sign(line[1] - line[0])
#         ia = 0
#         ib = 1
#         unsafe = 0
#         while ia < len(line) and ib < len(line):
#             # print(ia, ib)
#             a = line[ia]
#             b = line[ib]
#             diff = b - a
#             if 1 <= abs(diff) <= 3 and sign(diff) == dir:
#                 dir = sign(diff)
#                 ia = ib
#                 ib += 1
#                 continue
#             if ia == 0 and dir == sign(line[ib + 1] - line[ib]):
#                 ia = ib
#                 dir = sign(line[ib + 1] - line[ia])
#                 # print("ia", ia, dir)
#             ib += 1
#             unsafe += 1
#             if unsafe > 1:
#                 break
#         else:
#             ctr += 1
#             solved += [line]
#     return ctr, solved


def p2():
    ctr = 0
    for rl in LINES:
        for i in range(len(rl)):
            line = rl[:i] + rl[i + 1 :]
            dir = sign(line[1] - line[0])
            for a, b in zip(line[:-1], line[1:]):
                diff = b - a
                if 1 <= abs(diff) <= 3 and sign(diff) == dir:
                    continue
                break
            else:
                ctr += 1
                break
    return ctr


print("1:", p1())
print("2:", p2())
