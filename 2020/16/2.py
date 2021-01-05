def extract(l: list, idx: int) -> list:
    return [sl[idx] for sl in l]


ufields, uticket, unearby = open("input", "r").read().split("\n\n")

fields = {}
for field in ufields.splitlines():
    name, ranges = field.split(":")
    f1, f2 = ranges.split(" or ")
    f1 = list(map(int, f1.split("-")))
    f2 = list(map(int, f2.split("-")))
    f1 = list(range(f1[0], f1[1] + 1))
    f2 = list(range(f2[0], f2[1] + 1))
    fields[name.replace(" ", "_")] = f1 + f2

fs = []
for f in fields:
    fs += fields[f]
fieldset = set(fs)

nearbys = [list(map(int, nearby.split(","))) for nearby in unearby.splitlines()[1:]]
nb = []
ctr = 0
for i, nearby in enumerate(nearbys):
    b = True
    for val in nearby:
        if val not in fieldset:
            b = False
            break
    if b:
        nb.append(nearby)

cols = [extract(nb, i) for i in range(len(nb[0]))]
colMap = {}

for i, col in enumerate(cols):  # Loop over each col and check for possible matches
    colMap[i] = []
    for fid in fields:
        field = fields[fid]
        b = True
        for cv in col:
            if cv not in field:
                b = False
                break
        if b:
            colMap[i].append(fid)

# @Verzaukeks
fn = False
while not fn:
    fn = True
    for aid in colMap:
        if len(colMap[aid]) == 1:
            k = colMap[aid][0]
            for oid in colMap:
                if colMap[oid] != colMap[aid] and k in colMap[oid]:
                    colMap[oid].remove(k)
        else:
            fn = False

ticket = list(map(int, uticket.splitlines()[1].split(",")))

res = 1
for ci in colMap:
    if colMap[ci][0].startswith("departure"):
        res *= ticket[ci]

print(res)
