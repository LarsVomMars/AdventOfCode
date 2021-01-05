players = open("input", "r").read().split("\n\n")

p1, p2 = [list(map(int, p.splitlines()[1:])) for p in players]


def game(p1: list, p2: list) -> tuple:
    prev = set()
    while p1 and p2:
        plys = (tuple(p1), tuple(p2))
        if plys in prev:
            return True, p1
        prev.add(plys)
        p1v = p1.pop(0)
        p2v = p2.pop(0)
        ply = p1v > p2v
        if len(p1) >= p1v and len(p2) >= p2v:
            ply = game(p1[:p1v], p2[:p2v])[0]
        if ply:
            p1 += [p1v, p2v]
        else:
            p2 += [p2v, p1v]
    return (True, p1) if p1 else (False, p2)


ps = game(p1, p2)
res = 0
for idx, val in enumerate(ps[1][::-1]):
    res += val * (idx + 1)

print(res)
