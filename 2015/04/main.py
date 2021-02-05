from hashlib import md5 as hmd5
from itertools import count

key = "iwrupvqb"


def md5(s: str) -> str:
    return hmd5(s.encode("utf-8")).hexdigest()


def p(n: int) -> int:
    for x in count(1):
        if md5(key + str(x)).startswith("0" * n):
            return x


print("1:", p(5))
print("2:", p(6))
