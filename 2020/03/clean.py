rows = open("input", "r").readlines()


def search(right: int = 3, down: int = 1) -> int:
    trees = 0
    left = 0

    for i in range(0, len(rows), down):
        row = rows[i].strip()
        if row[left] == "#":
            trees += 1

        left = (left + right) % len(row)

    return trees


print("1:", res := search())
res *= search(1)
res *= search(5)
res *= search(7)
res *= search(1, 2)
print("2:", res)
