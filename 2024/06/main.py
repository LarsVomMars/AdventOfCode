LINES = [line.strip() for line in open("input").readlines()]

OBSTACLES = set()
GUARD = (0, 0)

ROWS = len(LINES)
COLS = len(LINES[0])

for y, line in enumerate(LINES):
    for x, char in enumerate(line):
        if char == "#":
            OBSTACLES.add((y, x))
        elif char == "^":
            GUARD = (y, x)


def get_dir(dir):
    return (dir[1], -dir[0])


def p1():
    visited = set()
    current = GUARD
    dir = (-1, 0)

    while 0 <= current[0] < ROWS and 0 <= current[1] < COLS:
        visited.add(current)
        new = (current[0] + dir[0], current[1] + dir[1])
        if new in OBSTACLES:
            dir = get_dir(dir)
        else:
            current = new
    return len(visited)


def p2():
    cnt = 0
    for y in range(ROWS):
        for x in range(COLS):
            if (y, x) in OBSTACLES:
                continue
            visited = set()
            current = GUARD
            dir = (-1, 0)

            current_obstacles = OBSTACLES | {(y, x)}

            while 0 <= current[0] < ROWS and 0 <= current[1] < COLS:
                new = (current[0] + dir[0], current[1] + dir[1])
                if new in current_obstacles:
                    dir = get_dir(dir)
                else:
                    visited.add((current, dir))
                    current = new

                if (current, dir) in visited:
                    cnt += 1
                    break

    return cnt


print("1:", p1())
print("2:", p2())
