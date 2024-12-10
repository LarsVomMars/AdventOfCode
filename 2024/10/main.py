LINES = [list(map(int, line.strip())) for line in open("input").readlines()]


def get_neighbors(y, x):
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(LINES) and 0 <= nx < len(LINES[0]):
            yield ny, nx


def bfs(start):
    s1 = 0
    s2 = 0
    to_visit = [start]
    visited = set()
    while to_visit:
        cur = to_visit.pop()
        curn = LINES[cur[0]][cur[1]]
        if curn == 9:
            # Accidentally implemented part 2 first :)
            if cur not in visited:
                visited.add(cur)
                s1 += 1
            s2 += 1
            continue
        nbs = get_neighbors(*cur)
        for ny, nx in nbs:
            if LINES[ny][nx] == curn + 1:
                to_visit.append((ny, nx))
    return s1, s2


def all():
    s1 = 0
    s2 = 0
    for y, line in enumerate(LINES):
        for x, c in enumerate(line):
            if c == 0:
                a, b = bfs((y, x))
                s1 += a
                s2 += b
    return s1, s2


p1, p2 = all()
print("1:", p1)
print("2:", p2)
