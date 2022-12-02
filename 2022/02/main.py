LINES = [line.strip().split() for line in open("input").readlines()]


SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

CHAR_MAP = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

REV_CHAR_MAP = {v: k for k, v in CHAR_MAP.items()}


def p1():
    score = 0
    for a, b in LINES:
        if a == CHAR_MAP[b]:
            score += SCORES[b] + 3
        elif a == "A" and CHAR_MAP[b] == "B" or a == "B" and CHAR_MAP[b] == "C" or a == "C" and CHAR_MAP[b] == "A":
            score += SCORES[b] + 6
        else:
            score += SCORES[b]
    return score


def p2():
    score = 0
    for a, b in LINES:
        if b == "X":
            if a == "A":
                score += 3
            elif a == "B":
                score += 1
            else:
                score += 2
        elif b == "Y":
            score += SCORES[REV_CHAR_MAP[a]] + 3
        else:
            score += SCORES[REV_CHAR_MAP[a]] % 3 + 1 + 6
    return score


print("1:", p1())
print("2:", p2())
