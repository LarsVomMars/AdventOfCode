from dataclasses import dataclass


@dataclass
class Pull:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    id: int
    pulls: list[Pull]


def str_to_pull(string):
    parts = string.split(",")
    red = 0
    green = 0
    blue = 0
    for part in parts:
        [amt, color] = part.split()
        match color:
            case "red":
                red = int(amt)
            case "green":
                green = int(amt)
            case "blue":
                blue = int(amt)
    return Pull(red, green, blue)


LINES = [line.strip() for line in open("input").readlines()]

GAMES: list[Game] = []
for line in LINES:
    id, pulls = line.split(":")
    id = int(id.split(" ")[1])
    pulls = pulls.split(";")
    pulls = [str_to_pull(pull) for pull in pulls]
    GAMES.append(Game(int(id), pulls))


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def max_pull(pulls):
    red = max([pull.red for pull in pulls])
    green = max([pull.green for pull in pulls])
    blue = max([pull.blue for pull in pulls])
    return [red, green, blue]


def eval_pulls(pulls):
    [red, green, blue] = max_pull(pulls)
    return red <= MAX_RED and green <= MAX_GREEN and blue <= MAX_BLUE


def p1():
    return sum([game.id for game in GAMES if eval_pulls(game.pulls)])


def p2():
    return sum(
        [rgb[0] * rgb[1] * rgb[2] for game in GAMES if (rgb := max_pull(game.pulls))]
    )


print("1:", p1())
print("2:", p2())
