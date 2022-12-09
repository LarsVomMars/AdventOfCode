from itertools import product


LINES = [line.strip().split() for line in open("input").readlines()]
ADJS = set(product(range(-1, 2), repeat=2))


def is_touching(head, tail):
    for a in ADJS:
        if (head[0] + a[0], head[1] + a[1]) == tail:
            return True


def simulate_head(head, dir):
    if dir == "U":
        head = (head[0], head[1] - 1)
    elif dir == "D":
        head = (head[0], head[1] + 1)
    elif dir == "L":
        head = (head[0] - 1, head[1])
    elif dir == "R":
        head = (head[0] + 1, head[1])

    return head


def sign(x):
    # return 1 if x > 0 else -1 if x < 0 else 0
    # Copilot be wildin
    return x // abs(x) if x else 0


def simulate_tail(head, tail):
    dx = sign(head[0] - tail[0])
    dy = sign(head[1] - tail[1])
    return tail[0] + dx, tail[1] + dy


def simulate_nrope(knots, moves):
    if knots < 2:
        return -1

    head = (0, 0)
    tail = [(0, 0) for _ in range(knots - 1)]

    visited = {tail[-1], }

    for dir, amt in moves:
        amt = int(amt)
        for _ in range(amt):
            head = simulate_head(head, dir)

            for i, tp in enumerate(tail):
                prev = tail[i - 1] if i > 0 else head

                if not is_touching(prev, tp):
                    tail[i] = simulate_tail(prev, tp)

            visited.add(tail[-1])

    return len(visited)


def p1():
    """
    Slightly faster version of p1 that doesn't use the generalized knot size thus eliminating the need for the nested loop and tail list

    head = (0, 0)
    tail = (0, 0)

    visited = {tail, }

    for dir, amt in LINES:
        amt = int(amt)
        for _ in range(amt):
            head = simulate_head(head, dir)

            if not is_touching(head, tail):
                tail = simulate_tail(head, tail)
                visited.add(tail)

    return len(visited)
    """
    return simulate_nrope(2, LINES)


def p2():
    return simulate_nrope(10, LINES)


print("1:", p1())
print("2:", p2())
