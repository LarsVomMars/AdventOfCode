LINES = [line.strip().split() for line in open("input").readlines()]


def run():
    cycles = []
    x = 1
    cycle = 0
    grid = ""
    for cmd, *arg in LINES:
        if cmd == "noop":
            grid += "#" if (cycle % 40) in range(x-1, x+2) else "."
            cycle += 1
            if cycle % 40 == 0:
                grid += "\n"
            if (cycle + 20) % 40 == 0:
                cycles.append(x * cycle)
        elif cmd == "addx":
            amt = int(arg[0])
            for _ in range(2):
                grid += "#" if (cycle % 40) in range(x-1, x+2) else "."
                cycle += 1
                if cycle % 40 == 0:
                    grid += "\n"
                if (cycle + 20) % 40 == 0:
                    cycles.append(x * cycle)
            x += amt

    return sum(cycles), "\n" + grid


a, b = run()
print("1:", a)
print("2:", b)
