def calc(num: int) -> int:
    return (num * SUBJECT) % REMAINDER


def run(hs: int) -> int:
    res = 0
    start = 1
    while start != hs:
        res += 1
        start = calc(start)
    return res


rows = [int(row.strip()) for row in open("input", "r").readlines()]

SUBJECT = 7
REMAINDER = 20201227

print(pow(rows[0], run(rows[1]), REMAINDER))
