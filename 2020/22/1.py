players = open("input", "r").read().split("\n\n")

p1, p2 = [list(map(int, p.splitlines()[1:])) for p in players]

while len(p1) > 0 and len(p2) > 0:
    p1v = p1.pop(0)
    p2v = p2.pop(0)
    if p1v > p2v:
        p1 += [p1v, p2v]
    elif p2v > p1v:
        p2 += [p2v, p1v]
    else:
        print("Shouldn't happen!")

res = 0
if len(p1) == 0:
    for idx, val in enumerate(p2[::-1]):
        res += val * (idx + 1)
elif len(p2) == 0:
    for idx, val in enumerate(p1[::-1]):
        res += val * (idx + 1)

print(res)
