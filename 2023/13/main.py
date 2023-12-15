data = open("input").read().split("\n\n")

PATTERNS = [
    (
        [[int(char == "#") for char in line.strip()] for line in pattern.splitlines()],
        [
            [int(line[i] == "#") for line in pattern.splitlines()]
            for i in range(len(pattern.splitlines()[0].strip()))
        ],
    )
    for pattern in data
]


def nested_xor(a, b):
    return [[x ^ y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def nested_sum(a):
    return sum(map(sum, a))


def solve():
    p1 = 0
    p2 = 0

    for rows, cols in PATTERNS:
        h = len(rows)
        w = len(cols)

        for i in range(1, w):
            size = min(i, w - i)
            c = cols[i - size : i]
            flipped_c = cols[i : i + size][::-1]
            diff = nested_sum(nested_xor(c, flipped_c))
            if diff == 0:
                p1 += i
            elif diff == 1:
                p2 += i

        for i in range(1, h):
            size = min(i, h - i)
            r = rows[i - size : i]
            flipped_r = rows[i : i + size][::-1]
            diff = nested_sum(nested_xor(r, flipped_r))
            if diff == 0:
                p1 += 100 * i
            if diff == 1:
                p2 += 100 * i
    return p1, p2


print(solve())
