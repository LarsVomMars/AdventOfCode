from collections import defaultdict
LINES = [line.strip() for line in open("input").readlines()]

START = LINES[0]
RPLS = {}

for line in LINES[2:]:
    base, res = line.split(" -> ")
    RPLS[base] = res


def chunk(s):
    return [s[i:i+2] for i in range(0, len(s)-1)]


def run(runs):
    s = START
    for _ in range(runs):
        new_s = ""
        cs = chunk(s)
        for c in cs:
            if c in RPLS:
                new_s += c[0] + RPLS[c]
            else:
                new_s += c[0]

        s = new_s + cs[-1][1]
    return s


def run_fast(runs):
    chars = defaultdict(int)
    for c in chunk(START):
        chars[c] += 1

    for i in range(runs):
        tmp = defaultdict(int)
        for key in chars:
            val = chars[key]
            tmp[key[0] + RPLS[key]] += val
            tmp[RPLS[key] + key[1]] += val

        chars = tmp.copy()
        tmp = defaultdict(int)
    return chars


def count(dd):
    cnt = defaultdict(int)
    for key, val in dd.items():
        cnt[key[0]] += val

    cnt[START[-1]] += 1
    return cnt


def p1():
    res = run_fast(10)
    cnt = count(res)
    return max(cnt.values()) - min(cnt.values())


def p2():
    res = run_fast(40)
    cnt = count(res)
    return max(cnt.values()) - min(cnt.values())


print("1:", p1())
print("2:", p2())
