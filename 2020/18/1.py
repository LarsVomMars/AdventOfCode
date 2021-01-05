import operator

rows = [row.strip() for row in open("input", "r").readlines()]

OPS = {
    "+": operator.add,
    "*": operator.mul,
}


def get_para_idx(toks):
    opn = 1
    for i, e in enumerate(toks):
        opn += 1 if e == "(" else -1 if e == ")" else 0
        if opn == 0:
            return i


def calc(toks):
    res = 0
    op = "+"
    while len(toks) > 0:
        tk = toks.pop(0)
        if tk in "(":
            idx = get_para_idx(toks)
            res = OPS[op](res, calc(toks[:idx + 1]))
            toks = toks[idx:]
        elif tk.isdigit():
            res = OPS[op](res, int(tk))
        elif tk in OPS.keys():
            op = tk
    return res


s = 0
for row in rows:
    row = row.replace("(", "( ").replace(")", " )")
    toks = row.split()
    s += calc(toks)
print(s)
