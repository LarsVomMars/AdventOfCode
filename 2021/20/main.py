from dataclasses import dataclass


@dataclass
class BoundingBox:
    top: int
    left: int
    bottom: int
    right: int

    def outside(self, x, y):
        return x < self.left or y < self.top or x > self.right or y > self.bottom

    def increase(self, amount=1):
        self.top -= amount
        self.left -= amount
        self.bottom += amount
        self.right += amount


lines = [line.strip() for line in open("input").readlines()]

ALGO = lines[0]
IMAGE_DATA = lines[2:]

IMAGE = {(x, y) for y, row in enumerate(IMAGE_DATA)
         for x, pix in enumerate(row) if pix == "#"}


def get_neighbors(x, y):
    for cy in range(-1, 2):
        for cx in range(-1, 2):
            yield x + cx, y + cy


def get_bit(image, x, y, boundary, lit=False):
    return "1" if (x, y) in image or boundary.outside(x, y) and lit else "0"


def enhance(image, boundary, lit=False):
    new = set()
    for y in range(boundary.top - 1, boundary.bottom + 2):
        for x in range(boundary.left - 1, boundary.right + 2):
            bin_num = int("".join(get_bit(image, nx, ny, boundary, lit)
                          for nx, ny in get_neighbors(x, y)), 2)
            if ALGO[bin_num] == "#":
                new.add((x, y))
    return new


def run(img):
    boundary = BoundingBox(0, 0, len(IMAGE_DATA) - 1, len(IMAGE_DATA[0]) - 1)
    for i in range(50):
        img = enhance(img, boundary, i % 2 == 1)
        boundary.increase()
        if i == 1:
            print("1:", len(img))
    print("2:", len(img))


run(IMAGE.copy())
