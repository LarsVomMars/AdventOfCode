ops1, ops2 = [[o for o in op.split(",")] for op in open("input", "r").readlines()]


def gen_positions(ops: list) -> set:
    pos = (0, 0)
    positions = {(0, 0)}
    for op in ops:
        dir = op[0]
        amt = int(op[1:])
        if dir == "R":
            pos = (pos[0] + amt, pos[1])
        elif dir == "L":
            pos = (pos[0] - amt, pos[1])
        elif dir == "U":
            pos = (pos[0], pos[1] + amt)
        elif dir == "D":
            pos = (pos[0], pos[1] - amt)
        positions.add(pos)
    return positions


def p1() -> int:
    min_dist = 1e5
    o1_pos = gen_positions(ops1)
    print(o1_pos)
    o2_pos = gen_positions(ops2)
    for pos in o1_pos:
        if pos in o2_pos:
            n_pos = abs(pos[0]) + abs(pos[1])
            print(pos)
            # min_dist = min(min_dist, n_pos)
    return min_dist


print("1:", p1())
