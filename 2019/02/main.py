opcodes = [int(c) for c in open("input", "r").read().split(",")]


def op(op: int, v1: int, v2: int):
    if op == 1:
        return v1 + v2
    elif op == 2:
        return v1 * v2
    elif op == 99:
        return -1
    else:
        print("Hmm")


def get_value(codes: list, pos: int) -> int:
    return codes[pos]


def p1(codes: list) -> int:
    for i in range(0, len(codes), 4):
        res_pos = codes[i + 3]
        if (res := op(codes[i], get_value(codes, codes[i + 1]), get_value(codes, codes[i + 2]))) >= 0:
            codes[res_pos] = res
        else:
            return codes[0]
    return codes[0]


def p2(codes: list) -> int:
    MEM = 19690720
    for v1 in range(100):
        for v2 in range(100):
            n_codes = codes.copy()
            n_codes[1] = v1
            n_codes[2] = v2
            if p1(n_codes) == MEM:
                return 100 * n_codes[1] + n_codes[2]


p1_codes = opcodes.copy()
p1_codes[1] = 12
p1_codes[2] = 2

print("1:", p1(p1_codes))
print("2:", p2(opcodes.copy()))
