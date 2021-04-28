opcodes = [int(c) for c in open("input", "r").read().split(",")]

def get_value(val: int, mode: int, codes: list):
    if mode == 0:
        return codes[val]
    elif mode == 1:
        return val


def int_computer(codes, inputs):
    pc = 0
    while pc < len(codes):
        code = str(codes[pc]).zfill(5)
        op = int(code[-2:])
        if op == 99:
            # print(codes)
            print("HALT!")
            return codes[0]
        elif op == 1:  # Addition
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            codes[int(codes[pc+3])] = v1 + v2
            pc += 4
        elif op == 2:  # Multiplication
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            codes[codes[pc+3]] = v1 * v2
            pc += 4
        elif op == 3:  # Input
            # v = int(input("gimme some input: "))
            v = inputs.pop(0)
            codes[codes[pc+1]] = v
            pc += 2
        elif op == 4:  # Output
            print("heres some output:", codes[codes[pc+1]])
            pc += 2
        elif op == 5:  # jump-if-true
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            if v1 != 0:
                pc = v2
            else:
                pc += 3
        elif op == 6:  # jump-if-false
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            # sets to value idk tho
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            if v1 == 0:
                pc = v2
            else:
                pc += 3
        elif op == 7:  # less than
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            codes[codes[pc+3]] = 1 if v1 < v2 else 0
            pc += 4
        elif op == 8:  # equals
            v1 = get_value(codes[pc+1], int(code[2]), codes)
            v2 = get_value(codes[pc+2], int(code[1]), codes)
            codes[codes[pc+3]] = 1 if v1 == v2 else 0
            pc += 4
        else:
            print("unknown op code:", op, "c", code, "at", pc)
            return
    print("overflow")

print("1 (input: 1):")
int_computer(opcodes.copy(), [1])
print("2 (input: 5):")
int_computer(opcodes.copy(), [5])
