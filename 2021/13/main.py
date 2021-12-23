import re
from copy import deepcopy


def print_grid(g):
    for row in g:
        print("".join(map(lambda b: "#" if b else " ", row)))
    print("\n")


file = open("input", "r").read()

POINTS = list(tuple(map(int, row)) for row in re.findall(r"(\d+),(\d+)", file))
FOLDS = re.findall(r"([xy])=(\d+)", file)

ROWS = max(POINTS, key=lambda x: x[1])[1] + 1
COLS = max(POINTS, key=lambda x: x[0])[0] + 1

GRID = [[False for _ in range(COLS)] for _ in range(ROWS)]

for x, y in POINTS:
    GRID[y][x] = True


def p1():
    new_grid = deepcopy(GRID)
    for fold in FOLDS:
        fold_dir = fold[0]
        fold_num = int(fold[1])
        if fold_dir == "y":
            up = new_grid[:fold_num]
            down = new_grid[fold_num+1:][::-1]
            new_grid = [[False for _ in range(len(up[0]))]
                        for _ in range(len(up))]

            for i, e in enumerate(up):
                for j, f in enumerate(e):
                    try:
                        new_grid[i][j] = f or down[i][j]
                    except IndexError:
                        new_grid[i][j] = f

        else:
            left = [row[:fold_num] for row in new_grid]
            right = [row[fold_num+1:][::-1] for row in new_grid]

            new_grid = [[False for _ in range(len(left[0]))]
                        for _ in range(len(left))]

            for i, e in enumerate(left):
                for j, f in enumerate(e):
                    try:
                        new_grid[i][j] = f or right[i][j]
                    except IndexError:
                        new_grid[i][j] = f

        return sum(sum(row) for row in new_grid)


def p2():
    new_grid = deepcopy(GRID)
    for fold in FOLDS:
        fold_dir = fold[0]
        fold_num = int(fold[1])
        if fold_dir == "y":
            up = new_grid[:fold_num]
            down = deepcopy(new_grid)
            new_grid = [[False for _ in range(len(up[0]))]
                        for _ in range(len(up))]

            for i, e in enumerate(up):
                for j, f in enumerate(e):
                    try:
                        new_grid[i][j] = f or down[2 * fold_num - i][j]
                    except IndexError:
                        new_grid[i][j] = f

        else:
            left = [row[:fold_num] for row in new_grid]
            right = deepcopy(new_grid)

            new_grid = [[False for _ in range(len(left[0]))]
                        for _ in range(len(left))]

            for i, e in enumerate(left):
                for j, f in enumerate(e):
                    try:
                        new_grid[i][j] = f or right[i][2 * fold_num - j]
                    except IndexError:
                        print("BHH")
                        new_grid[i][j] = f
    print("\n")
    print_grid(new_grid)


print("1:", p1())
p2()
