from dataclasses import dataclass


INPUT = open("input").read().strip()


def p1():
    # TODO: Speed up
    disk = []
    id = 0
    flip = True
    for e in INPUT:
        disk += [id if flip else None] * int(e)
        id += flip
        flip = not flip
    while None in disk:
        last = disk.pop(-1)
        if last is None:
            continue
        idx = disk.index(None)
        disk[idx] = last
    return sum(i * e for i, e in enumerate(disk))


@dataclass
class Block:
    id: int
    start: int
    length: int


def p2():
    disk = []
    free = []
    start = 0
    id = 0
    flip = True
    for e in INPUT:
        e = int(e)
        if flip:
            disk.append(Block(id, start, e))
            id += 1
        else:
            free.append(Block(-1, start, e))
        start += e
        flip = not flip

    for block in disk[::-1]:
        for f in free:
            if f.start >= block.start:
                break
            if f.length >= block.length:
                block.start = f.start
                f.start += block.length
                f.length -= block.length
                break
    return sum(
        sum(range(block.start, block.start + block.length)) * block.id for block in disk
    )


print("1:", p1())
print("2:", p2())
