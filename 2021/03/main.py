from collections import Counter

LINES = [line.strip() for line in open("input").readlines()]
COLS = [[row[i] for row in LINES] for i in range(len(LINES[0]))]


def p1():
    gamma = ""
    epsilon = ""
    for col in COLS:
        c = Counter(col).most_common()
        gamma += c[0][0]
        epsilon += c[-1][0]

    return int(gamma, 2) * int(epsilon, 2)


def p2():
    ox = -1
    co = -1
    ox_l = LINES
    co_l = LINES
    for i in range(len(LINES[0])):
        if ox == -1:
            ox_c = Counter([row[i] for row in ox_l]).most_common()
            if len(ox_c) == 1:
                ox_c += ("", 0)
            m, l = ox_c
            f = m if m[1] > l[1] else l if l[1] > m[1] else "1"
            ox_l = list(filter(lambda x: x[i] == f[0], ox_l))

            if ox != -1 or len(ox_l) == 1:
                ox = int(ox_l[0], 2)

        if co == -1:
            co_c = Counter([row[i] for row in co_l]).most_common()
            if len(co_c) == 1:
                co_c += ("", 0)
            m, l = co_c
            f = m if m[1] < l[1] else l if l[1] < m[1] else "0"
            co_l = list(filter(lambda x: x[i] == f[0], co_l))

            if co != -1 or len(co_l) == 1:
                co = int(co_l[0], 2)

    return ox * co


print("1:", p1())
print("2:", p2())
