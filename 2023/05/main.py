import re

REG_SEED = re.compile(r"(\d+)")
REG_MAPS = re.compile(r"(\d+) (\d+) (\d+)")


class DefaultMap:
    def __init__(self, block: str):
        self.data = [
            (s, d - s, s + l)
            for d, s, l in map(lambda x: map(int, x), REG_MAPS.findall(block))
        ]

    def __getitem__(self, key):
        for source, diff, end in self.data:
            if source <= key < end:
                return key + diff
        return key

    def get_range(self, rng):
        res = []
        to_check = rng
        for source, diff, end in self.data:
            outer = []
            while to_check:
                (r_start, r_end) = to_check.pop()
                if r_start < source:
                    outer.append((r_start, min(r_end, source)))
                if end < r_end:
                    outer.append((max(r_start, end), r_end))
                if r_start < end and source < r_end:
                    res.append((max(r_start, source) + diff, min(r_end, end) + diff))
            to_check = outer
        return res + to_check


seeds, *maps = [line.strip() for line in open("input").read().split("\n\n")]
SEEDS = list(map(int, REG_SEED.findall(seeds)))
MAPS = list(map(DefaultMap, maps))


def p1():
    res = []
    for seed in SEEDS:
        value = seed
        for m in MAPS:
            value = m[value]
        res.append(value)
    return min(res)


def p2():
    res = []
    seeds = [(SEEDS[i], SEEDS[i] + SEEDS[i + 1]) for i in range(0, len(SEEDS) - 1, 2)]

    for seed in seeds:
        value = [seed]
        for m in MAPS:
            value = m.get_range(value)
        res.append(min(value, key=lambda x: x[0])[0])
    return min(res)


print("1:", p1())
print("2:", p2())
