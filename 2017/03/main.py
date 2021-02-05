from math import isqrt, ceil

num = 368078


def p1():
    # num = 1024 # Isn't working for every number
    ring = ceil(isqrt(num) / 2)
    ring_len = ring * 2 + 1
    pos = num % ring_len
    mid = ceil(ring_len / 2 - pos)
    return ring + mid


def p2():
    pass


print("1:", p1())
print("2:", p2())
