import re
from itertools import islice, product
from functools import cache

STARTING_POS = list(map(int, re.findall(r": (\d+)", open("input").read())))


def nicer_dicer():
    dice = 0
    while True:
        yield (dice := dice % 100 + 1)


def take(dice, amt=3):
    return sum(islice(dice, amt))


def p1():
    dice = nicer_dicer()
    dice_throws = 0
    scores = [0, 0]
    current = 0
    positions = STARTING_POS.copy()

    while max(scores) < 1000:
        sm = take(dice)
        dice_throws += 3
        positions[current] = (positions[current] + sm - 1) % 10 + 1
        scores[current] += positions[current]
        current ^= 1

    return min(scores) * dice_throws


POSSIBILITIES = [i+j+k for i in range(1, 4)
                 for j in range(1, 4) for k in range(1, 4)]


@cache
def quantum_game(position, score, turn=True):
    if max(score) >= 21:
        return score[0] > score[1], score[0] < score[1]

    pos = position[0] if turn else position[1]
    new_positions = [(pos + throw - 1) % 10 + 1 for throw in POSSIBILITIES]
    games = [
        quantum_game(
            (new_pos if turn else position[0], position[1] if turn else new_pos),
            (score[0] + new_pos * int(turn),
             score[1] + new_pos * int(not turn)),
            not turn
        )
        for new_pos in new_positions
    ]
    game_score = [0, 0]
    for a, b in games:
        game_score[0] += a
        game_score[1] += b
    return tuple(game_score)


def p2():
    return max(quantum_game(tuple(STARTING_POS), (0, 0)))


print("1:", p1())
print("2:", p2())
