rows = [row.strip() for row in open("input", "r")]

black_tiles = []

for row in rows:
    i = 0
    #   +:  ne  e  se
    #   -:  sw  w  nw
    t_pos = [0, 0, 0]
    while i < len(row):
        c = row[i]
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
    if t_pos in black_tiles:
        black_tiles.remove(t_pos)
    else:
        black_tiles.append(t_pos)

print(len(black_tiles))
