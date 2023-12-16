lines = [line.strip() for line in open("input")]

MIRRORS = {
    (y, x): char
    for y, line in enumerate(lines)
    for x, char in enumerate(line)
    if char != "."
}

START = (0, 0)

HEIGHT = len(lines)
WIDTH = len(lines[0])


def energize(start, init_dir):
    to_visit = [((start[0] - init_dir[0], start[1] - init_dir[1]), init_dir)]
    visited = set()

    while to_visit:
        node = to_visit.pop(0)
        if node in visited:
            continue
        visited.add(node)
        pos, dir = node
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if not (0 <= new_pos[0] < HEIGHT and 0 <= new_pos[1] < WIDTH):
            continue
        if new_pos in MIRRORS:
            mirror = MIRRORS[new_pos]
            match mirror:
                case "-":
                    if dir[0] == 0:
                        to_visit.append((new_pos, dir))
                    else:
                        to_visit.append((new_pos, (0, 1)))
                        to_visit.append((new_pos, (0, -1)))
                case "|":
                    if dir[1] == 0:
                        to_visit.append((new_pos, dir))
                    else:
                        to_visit.append((new_pos, (1, 0)))
                        to_visit.append((new_pos, (-1, 0)))
                case "/":
                    if dir[0] == 0:
                        to_visit.append((new_pos, (-dir[1], 0)))
                    else:
                        to_visit.append((new_pos, (0, -dir[0])))
                case "\\":
                    if dir[0] == 0:
                        to_visit.append((new_pos, (dir[1], 0)))
                    else:
                        to_visit.append((new_pos, (0, dir[0])))
        elif 0 <= new_pos[0] < HEIGHT and 0 <= new_pos[1] < WIDTH:
            to_visit.append((new_pos, dir))

    return len(set(map(lambda x: x[0], visited))) - 1


def p1():
    return energize(START, (0, 1))


def p2():
    score = []
    for i in range(HEIGHT):
        score.append(energize((i, 0), (0, 1)))
        score.append(energize((i, WIDTH - 1), (0, -1)))

    for i in range(WIDTH):
        score.append(energize((0, i), (1, 0)))
        score.append(energize((HEIGHT - 1, i), (-1, 0)))

    return max(score)


print("1:", p1())
print("2:", p2())
