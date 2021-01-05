rows = [row.strip() for row in open("input", "r").readlines()]


def get_para_idx(toks):
    opn = 1
    for i, e in enumerate(toks):
        opn += 1 if e == "(" else -1 if e == ")" else 0
        if opn == 0:
            return i


def calc(toks):
    while "(" in toks:  # Recursive wohoo
        i = toks.index("(")
        ci = get_para_idx(toks[i + 1:]) + i + 1
        toks = toks[:i] + str(calc(toks[i + 1:ci])) + toks[ci + 1:]
    toks = toks.split()
    while "+" in toks:  # Apply + before *
        i = toks.index("+")
        toks[i - 1:i + 2] = [f"{int(toks[i - 1]) + int(toks[i + 1])}"]
    return eval(" ".join(toks))  # Eval wohoo


s = 0
for row in rows:
    s += calc(row)
print(s)
