LINES = [line.strip() for line in open("input").readlines()]


def get_char_num(char: str):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


def p1():
    score = 0
    for line in LINES:
        a, b = line[:len(line)//2], line[len(line)//2:]
        c = set(a).intersection(set(b))
        score += get_char_num(c.pop())

    return score


def p2():
    score = 0
    lines = list(zip(*[iter(LINES)]*3))
    for a, b, c in lines:  # type: ignore
        d = set(a).intersection(set(b)).intersection(set(c))
        score += get_char_num(d.pop())
    return score


print("1:", p1())
print("2:", p2())
