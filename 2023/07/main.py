from collections import Counter
from functools import cmp_to_key

LINES = [
    (r[0], int(r[1]))
    for line in open("input").readlines()
    if (r := line.strip().split())
]


def get_type(deck, part2):
    jokers = 0
    if part2:
        jokers = deck.count("J")
        deck = deck.replace("J", "")

    cards = sorted(Counter(deck).values())
    l = len(cards)

    if l <= 1:
        return 6
    most = cards[-1] + jokers

    if l >= 4:
        return 5 - l
    if l == 2:
        return most + 1
    if l == 3:
        return most


def get_value(card, part2):
    match card:
        case "T":
            return 10
        case "J":
            return 1 if part2 else 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _:
            return int(card)


def make_cmp(part2):
    def cmp_total(a, b):
        cmp = get_type(a[0], part2) - get_type(b[0], part2)
        if cmp != 0:
            return cmp
        for c, d in zip(a[0], b[0]):
            if c != d:
                return get_value(c, part2) - get_value(d, part2)
        return 0

    return cmp_total


def solve(part2):
    return sum(
        [
            bid * i
            for i, (_, bid) in enumerate(
                sorted(LINES, key=cmp_to_key(make_cmp(part2))), 1
            )
        ]
    )


def p1():
    return solve(False)


def p2():
    return solve(True)


print("1:", p1())
print("2:", p2())
