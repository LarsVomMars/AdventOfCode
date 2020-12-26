rows = open("input", "r").readlines()
data = list("".join([row.strip() for row in rows]))
ROW_LENGTH = len(rows[0].strip())

ADJ = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def check(data: list, i: int) -> int:
    ctr = 0
    for pos in ADJ:
        np = i + (pos[0] * ROW_LENGTH + pos[1])
        rp = i % ROW_LENGTH
        if not 0 <= np < len(data) or not 0 <= rp + pos[1] < ROW_LENGTH:
            continue
        ctr += 1 if data[np] == "#" else 0
    return ctr


prev = []
ctr = 0

while prev != data:
    prev = data.copy()
    ndata = data.copy()
    for i in range(len(data)):
        char = data[i]
        if char == ".":
            continue
        oc = check(data, i)
        if oc >= 4 and char == "#":
            ndata[i] = "L"
        elif oc == 0 and char == "L":
            ndata[i] = "#"
    data = ndata.copy()

print(data.count("#"))
