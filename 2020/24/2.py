from itertools import chain

# Day 17 flashbacks
rows = [row.strip() for row in open("input", "r")]
NB_POS = [(1, -1, 0), (-1, 1, 0), (0, -1, 1), (0, 1, -1), (-1, 0, 1), (1, 0, -1)]


def get_neighbours(pos: tuple) -> set:
    for p in NB_POS:
        yield tuple(map(lambda x, y: x + y, pos, p))


def check(act: set, pos: tuple) -> bool:
    nbs = get_neighbours(pos)
    ctr = sum([1 for nb in nbs if act.__contains__(nb)])
    return ctr == 2 or (pos in act and ctr == 1)


active = set()
for row in rows:
    i = 0
    #   +:  ne  e  se
    #   -:  sw  w  nw
    t_pos = [0, 0, 0]
    while i < len(row):
        c = row[i]
        # There might be a better solution
        if c in ["e", "w"]:
            t_pos[0] += 1 if c == "e" else -1
            t_pos[1] -= 1 if c == "e" else -1
            i += 1
        else:
            nc = row[i + 1]
            if (c + nc) in ["ne", "sw"]:
                t_pos[0] += 1 if c == "n" else -1
                t_pos[2] -= 1 if c == "n" else -1
            elif (c + nc) in ["se", "nw"]:
                t_pos[1] -= 1 if c == "s" else -1
                t_pos[2] += 1 if c == "s" else -1
            i += 2
    t_pos = tuple(t_pos)
    if t_pos in active:
        active.discard(t_pos)
    else:
        active.add(t_pos)

for _ in range(100):
    testable = set(chain.from_iterable(get_neighbours(pos) for pos in active))
    active = {pos for pos in testable if check(active, pos)}

print(len(active))
