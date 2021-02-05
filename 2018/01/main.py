rows = [row.strip() for row in open("input", "r").readlines()]


def p1():
    return eval("".join(rows))


def p2():
    # rows = ["+7", "+7", "-2", "-7", "-4"]
    l = [0]
    i = 0
    while True:
        r = rows[i % len(rows)]
        val = eval(f"{l[-1]}+{r}")
        if val in l:
            return val
        l.append(val)
        i += 1


print("1:", p1())
print("2:", p2())
