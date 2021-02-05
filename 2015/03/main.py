instructions = open("input", "r").read().strip()

instruction_map = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def add_pos(pos: tuple, mv: tuple) -> tuple:
    return pos[0] + mv[0], pos[1] + mv[1]


def p1():
    visited = {(0, 0)}
    pos = (0, 0)
    for ins in instructions:
        mv = instruction_map[ins]
        pos = add_pos(pos, mv)
        visited.add(pos)
    return visited


def p2():
    visited = {(0, 0)}
    s_pos = (0, 0)
    r_pos = (0, 0)
    turn = True
    for ins in instructions:
        mv = instruction_map[ins]
        if turn:
            s_pos = add_pos(s_pos, mv)
            turn = False
            visited.add(s_pos)
        else:
            r_pos = add_pos(r_pos, mv)
            turn = True
            visited.add(r_pos)
    return visited


print("1:", len(p1()))
print("2:", len(p2()))
