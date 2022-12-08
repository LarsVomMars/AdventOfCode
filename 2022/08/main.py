LINES = [tuple(map(int, list(line.strip())))
         for line in open("input").readlines()]


def get_col(j):
    return [row[j] for row in LINES]


def p1():
    visible = 0
    for i, row in enumerate(LINES):
        for j, coli in enumerate(row):
            left = row[:j]
            if all(c < coli for c in left):
                visible += 1
                continue

            if j < len(row):
                right = row[j + 1:]
                if all(c < coli for c in right):
                    visible += 1
                    continue

            col = get_col(j)
            top = col[:i]
            if all(c < coli for c in top):
                visible += 1
                continue

            if i < len(col):
                bottom = col[i + 1:]
                if all(c < coli for c in bottom):
                    visible += 1
                    continue

    return visible


def p2():
    max_score = 0
    for i, row in enumerate(LINES):
        for j, coli in enumerate(row):
            score = 1
            if j > 0:
                sl = 0
                left = row[:j]
                for c in left[::-1]:
                    sl += 1
                    if c >= coli:
                        break
                score *= sl
            else:
                continue

            if j < len(row):
                sr = 0
                right = row[j + 1:]
                for c in right:
                    sr += 1
                    if c >= coli:
                        break
                score *= sr
            else:
                continue

            col = get_col(j)
            if i > 0:
                top = col[:i]
                st = 0

                for c in top[::-1]:
                    st += 1
                    if c >= coli:
                        break
                score *= st
            else:
                continue

            if i < len(col):
                bottom = col[i + 1:]
                sb = 0
                for c in bottom:
                    sb += 1
                    if c >= coli:
                        break
                score *= sb
            else:
                continue

            max_score = max(max_score, score)
    return max_score


print("1:", p1())
print("2:", p2())
