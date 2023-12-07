from collections import Counter
from enum import IntEnum
from functools import cmp_to_key

LINES = [
    (r[0], int(r[1]))
    for line in open("input").readlines()
    if (r := line.strip().split())
]


class CardType(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def get_type(deck, part2=False):
    jokers = 0
    if part2:
        jokers = deck.count("J")
        deck = deck.replace("J", "")

    cards = sorted(Counter(deck).values())

    if len(cards) <= 1:
        return CardType.FIVE_OF_A_KIND

    most = cards[-1] + jokers

    if len(cards) == 5:
        return CardType.HIGH_CARD
    if len(cards) == 4:
        return CardType.PAIR

    if len(cards) == 2 and most == 4:
        return CardType.FOUR_OF_A_KIND
    if len(cards) == 2 and most == 3:
        return CardType.FULL_HOUSE

    if len(cards) == 3 and most == 3:
        return CardType.THREE_OF_A_KIND
    if len(cards) == 3 and most == 2:
        return CardType.TWO_PAIR


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
    values = sorted(LINES, key=cmp_to_key(make_cmp(part2)))
    return sum([bid * i for i, (_, bid) in enumerate(values, 1)])


def p1():
    return solve(False)


def p2():
    return solve(True)


print("1:", p1())
print("2:", p2())
