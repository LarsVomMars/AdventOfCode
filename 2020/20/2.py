# DISCLAIMER: Wasn't able to solve this myself to 100%
# So I did some modifications to https://github.com/arknave/advent-of-code-2020/blob/main/day20/day20.py
from copy import deepcopy
from math import isqrt


def rotate(matrix: list) -> list:
    matrix = deepcopy(matrix)
    n = len(matrix)
    matrix.reverse()
    for x in range(n):
        for y in range(n - 1, x - 1, -1):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    return matrix


def flip(matrix: list) -> list:
    matrix = deepcopy(matrix)
    return matrix[::-1]


def place(matrix: list, i: int, j: int, block: list):
    n = len(block)
    for x in range(n):
        for y in range(n):
            matrix[i + x][j + y] = block[x][y]


data = open("input", "r").read().split("\n\n")
tiles = {}
for tile in data:
    name, *rows = tile.strip().splitlines()
    tile_id = int(name[-5:-1])
    rotations = [grid := list(list(l) for l in rows)]
    for _ in range(2):
        for _ in range(4):
            rotations.append(grid := rotate(grid))
        grid = flip(grid)
    tiles[tile_id] = rotations

N = isqrt(len(tiles.values()))
K = len(list(tiles.values())[0][0])
stitched = [[None for _ in range(N * K)] for _ in range(N * K)]
placed = set()


def place_tiles(rowi: int = 0, coli: int = 0):
    if coli == N:
        return place_tiles(rowi + 1, 0)
    if rowi == N:
        return True

    for tile_id in tiles:
        if tile_id in placed:
            continue
        tile = tiles[tile_id]
        placed.add(tile_id)
        for tile_rot in tile:
            place(stitched, K * rowi, K * coli, tile_rot)
            can_place = True
            if rowi > 0:
                top = tile_rot[0]
                before = stitched[K * rowi - 1][K * coli:K * coli + K]
                can_place &= top == before
            if coli > 0:
                left = [row[0] for row in tile_rot]
                before = [stitched[row][K * coli - 1] for row in range(K * rowi, K * rowi + K)]
                can_place &= left == before
            if can_place and place_tiles(rowi, coli + 1):
                return True
        placed.remove(tile_id)
    return False


place_tiles()
out = [[]]
for i in range(N * K):
    for j in range(N * K):
        if i % K in (0, K - 1) or j % K in (0, K - 1):
            continue
        if len(out[-1]) == N * (K - 2):
            out.append([])
        out[-1].append(stitched[i][j])

monster = [
    (0, 18),
    (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
    (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
]
ans = 0
for _ in range(2):
    for _ in range(4):
        monster_count = 0
        for i in range(len(out) - 2):
            for j in range(len(out[0]) - 19):
                if all(out[i + dx][j + dy] == '#' for dx, dy in monster):
                    monster_count += 1
        ans = max(ans, monster_count)
        out = rotate(out)
    out = flip(out)

print("".join("".join(o) for o in out).count("#") - ans * len(monster))
