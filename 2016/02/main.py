instructions = [row.strip() for row in open("input", "r").readlines()]


def get_code(instruction: str, key_pad: list) -> str:
    row = 1
    col = 1
    for c in instruction:
        if c == "U":
            row -= 1 if row > 0 else 0
        elif c == "D":
            row += 1 if row < 2 else 0
        elif c == "L":
            col -= 1 if col > 0 else 0
        elif c == "R":
            col += 1 if col < 2 else 0

    return str(key_pad[row][col])


def p1(instruction: str) -> str:
    key_pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return get_code(instruction, key_pad)


print("1:", "".join(map(p1, instructions)))
