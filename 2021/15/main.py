from heapq import heappop, heappush

LINES = [line.strip() for line in open("input").readlines()]

GRID = [
    [int(c) for c in line] for line in LINES
]


def extend_grid(grid, size=5):
    return [[
        (x+i+j - 1) % 9 + 1 for i in range(size) for x in row
    ] for j in range(size) for row in grid]


def dijkstra(data):
    nbs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = (0, 0)
    end = (len(data)-1, len(data[0])-1)

    queue = []
    heappush(queue, (start, 0))

    distances = {}

    while len(queue) > 0:
        pos, weight = heappop(queue)
        if pos == end:
            return weight

        for y, x in map(lambda p: (pos[0]+p[0], pos[1]+p[1]), nbs):
            if x < 0 or y < 0 or y > end[0] or x > end[1]:
                continue
            new_weight = weight + data[y][x]
            if (y, x) in distances and distances[(y, x)] <= new_weight:
                continue
            distances[(y, x)] = new_weight
            heappush(queue, ((y, x), new_weight))


def p1():
    return dijkstra(GRID)


def p2():
    return dijkstra(extend_grid(GRID))


print("1:", p1())
print("2:", p2())
