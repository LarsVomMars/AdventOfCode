from itertools import product, chain

rows = [row.strip() for row in open("input", "r").readlines()]

COL_LEN = len(rows)
ROW_LEN = len(rows[0])

active = {
    (x, y, 0)
    for x, y in product(range(COL_LEN), range(ROW_LEN)) if rows[x][y] == "#"
}


def get_neighbours(pos: tuple) -> set:
    adjs = set(product(range(-1, 2), repeat=3)) - {(0, 0, 0)}
    return {tuple(a + b for a, b in zip(pos, adjc)) for adjc in adjs}


def check(act: set, pos: tuple) -> bool:
    ctr = 0
    nbs = get_neighbours(pos)
    ctr = sum([1 if act_pos in nbs else 0 for act_pos in act])
    return ctr == 3 or (pos in act and ctr == 2)


for _ in range(6):
    testable = set(chain.from_iterable(get_neighbours(pos)
                                       for pos in active)) | active
    active = {pos for pos in testable if check(active, pos)}

print(len(active))
