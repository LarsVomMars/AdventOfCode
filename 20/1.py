tile_data = open("input", "r").read().split("\n\n")

edges = {}

for tile in tile_data:
    name, *rows = [t.strip() for t in tile.splitlines()]
    name = name[-5:-1]

    right = "".join([r[len(r) - 1] for r in rows])
    left = "".join([r[0] for r in rows])

    edges[name] = [rows[0], right, rows[len(rows) - 1], left]

for tile_i1 in edges:
    for tile_i2 in edges:
        if tile_i1 == tile_i2:
            continue
        for i, side in enumerate(edges[tile_i1]):
            if side == "":
                continue
            idx = -1
            if side in edges[tile_i2]:
                idx = edges[tile_i2].index(side)
            elif side[::-1] in edges[tile_i2]:
                idx = edges[tile_i2].index(side[::-1])

            if idx == -1:
                continue

            edges[tile_i1][i] = ""
            edges[tile_i2][idx] = ""

res = 1
for ti in edges:
    if len(edges[ti]) - edges[ti].count("") == 2:
        res *= int(ti)
print(res)
