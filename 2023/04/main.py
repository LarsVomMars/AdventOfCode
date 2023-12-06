import re

LINES = [line.strip() for line in open("input").readlines()]

reg = re.compile(r"\d+")

GAMES = []
for line in LINES:
    game, nums = line.split(":")
    game = int(reg.findall(game)[0])
    winning, having = nums.split("|")
    matches = set(reg.findall(winning)) & set(reg.findall(having))
    GAMES.append((game, matches))


def p1():
    return sum([2 ** (len(nums) - 1) for _, nums in GAMES if len(nums) > 0])


def p2():
    cards = [1] * len(GAMES)

    for game, matches in GAMES:
        for i in range(game, game + len(matches)):
            cards[i] += cards[game - 1]
    return sum(cards)


print("1:", p1())
print("2:", p2())
