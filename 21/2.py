rows = [row.strip() for row in open("input", "r")]

allergens = {}
foods = []
for line in rows:
    pi = line.index("(")
    ingrs = set(line[:pi].split())
    algns = [e.strip(",") for e in line[pi + 1:-1].split()[1:]]
    for algn in algns:
        if algn in allergens:
            allergens[algn] &= ingrs
        else:
            allergens[algn] = set(ingrs)
    foods.append((ingrs, algns))

bad = set()
for v in allergens.values():
    bad |= v

# See 16.2 - however this works :D
fn = False
while not fn:
    fn = True
    for aid in allergens:
        if len(allergens[aid]) == 1:
            k = list(allergens[aid])[0]
            for oid in allergens:
                if allergens[oid] != allergens[aid] and k in allergens[oid]:
                    allergens[oid].remove(k)
        else:
            fn = False

sorted_allergens = sorted([ingr for ingr in allergens.keys()])
print(",".join([list(allergens[alg])[0] for alg in sorted_allergens]))
