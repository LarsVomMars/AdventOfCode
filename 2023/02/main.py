import re

LINES = [line.strip() for line in open("input").readlines()]

game_reg = re.compile(r"Game (\d+)")
red_reg = re.compile(r"(\d+) red")
green_reg = re.compile(r"(\d+) green")
blue_reg = re.compile(r"(\d+) blue")

GAMES = []
for line in LINES:
    id = int(game_reg.match(line).group(1))
    red = max(map(int, red_reg.findall(line)))
    green = max(map(int, green_reg.findall(line)))
    blue = max(map(int, blue_reg.findall(line)))
    GAMES.append((int(id), (red, green, blue)))


def p1():
    return sum(
        [id for id, rgb in GAMES if rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14]
    )


def p2():
    return sum([rgb[0] * rgb[1] * rgb[2] for _, rgb in GAMES])


print("1:", p1())
print("2:", p2())
