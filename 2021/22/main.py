import re
from dataclasses import dataclass

data = open("input").read()


@dataclass
class Cuboid:
    state: bool
    sx: int
    ex: int
    sy: int
    ey: int
    sz: int
    ez: int

    def get_overlap(self, c2):
        return Cuboid(
            not c2.state,
            max(self.sx, c2.sx), min(self.ex, c2.ex),
            max(self.sy, c2.sy), min(self.ey, c2.ey),
            max(self.sz, c2.sz), min(self.ez, c2.ez)
        )

    def size(self):
        return (self.ex - self.sx + 1) * (self.ey - self.sy + 1) * (self.ez - self.sz + 1)


cuboids = list(
    map(
        lambda x: Cuboid(x[0] == "on", *tuple(map(int, x[1:]))),
        re.findall(
            r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", data)
    )
)


def p1(cuboids):
    grid = [[[False for _ in range(101)]
             for _ in range(101)] for _ in range(101)]

    for cb in cuboids[:20]:
        for x in range(cb.sx, cb.ex + 1):
            for y in range(cb.sy, cb.ey + 1):
                for z in range(cb.sz, cb.ez + 1):
                    grid[x][y][z] = cb.state
    return sum(sum(sum(i for i in r) for r in c) for c in grid)


def validate_overlap(ovl):
    return ovl.sx <= ovl.ex and ovl.sy <= ovl.ey and ovl.sz <= ovl.ez


def p2(cuboids):
    cbs = []
    for cuboid in cuboids:
        overlaps = list(
            filter(validate_overlap, [cuboid.get_overlap(cb2) for cb2 in cbs]))
        cbs.extend(overlaps)
        if cuboid.state:
            cbs.append(cuboid)

    return sum(map(lambda x: x.size() * (1 if x.state else -1), cbs))


print("1:", p1(cuboids))
print("2:", p2(cuboids))
