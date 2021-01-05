from itertools import product, chain

rows = [row.strip() for row in open("input", "r").readlines()]


def solve(dimensions: int = 3):
    col_len = len(rows)
    row_len = len(rows[0])

    active = {
        (x, y) + (0,) * (dimensions - 2)
        for x, y in product(range(col_len), range(row_len)) if rows[x][y] == "#"
    }

    def get_neighbours(pos: tuple) -> set:
        adjs = set(product(range(-1, 2), repeat=dimensions)) - {(0,) * dimensions}
        return {tuple(a + b for a, b in zip(pos, adjc)) for adjc in adjs}

    def check(act: set, pos: tuple) -> bool:
        nbs = get_neighbours(pos)
        ctr = sum([1 if act_pos in nbs else 0 for act_pos in act])
        return ctr == 3 or (pos in act and ctr == 2)

    for _ in range(6):
        testable = set(chain.from_iterable(get_neighbours(pos) for pos in active)) | active
        active = {pos for pos in testable if check(active, pos)}

    return len(active)


print("1:", solve(3))
print("2:", solve(4))
