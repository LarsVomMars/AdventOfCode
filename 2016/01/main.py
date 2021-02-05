instructions = [inst.strip() for inst in open("input", "r").read().split(",")]


def p1(instructs: list) -> int:
    face = [0, 1]
    pos = (0, 0)
    for inst in instructs:
        mv = inst[0]
        amt = int(inst[1:])
        if mv == "L":
            face[0], face[1] = face[1], -face[0]
        elif mv == "R":
            face[1], face[0] = face[0], -face[1]

        pos = (pos[0] + amt * face[0], pos[1] + amt * face[1])
    return abs(pos[0]) + abs(pos[1])


def p2(instructs: list) -> int:
    face = [0, 1]
    pos = [0, 0]
    visited = {tuple(pos)}
    for inst in instructs:
        mv = inst[0]
        amt = int(inst[1:])
        if mv == "L":
            face[0], face[1] = face[1], -face[0]
        elif mv == "R":
            face[1], face[0] = face[0], -face[1]

        for _ in range(amt):
            pos[0] += face[0]
            pos[1] += face[1]
            if tuple(pos) in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(tuple(pos))


print("1:", p1(instructions))
print("2:", p2(instructions))
