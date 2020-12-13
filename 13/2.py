# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


times = open("input", "r").readlines()[1].split(",")

"""
set 17,x,13,19 => 3417
all are (co-)prime
-> chinese remainder theorem
"""

nums = []
rems = []
for i, char in enumerate(times):
    if char == 'x':
        continue
    num = int(char)
    rems.append(num - i % num)
    nums.append(num)

print(chinese_remainder(nums, rems))
