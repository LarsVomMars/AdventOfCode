rows = [row.strip() for row in open("input", "r")]

allergens = {}
foods = []
for line in rows:
    pi = line.index("(")
    ingr = set(line[:pi].split())
    algn = [e.strip(",") for e in line[pi + 1:-1].split()[1:]]
    for alg in algn:
        if alg in allergens:
            allergens[alg] &= ingr
        else:
            allergens[alg] = set(ingr)
    foods.append((ingr, algn))

bad = set()
for v in allergens.values():
    bad |= v

print(sum(1 for ingrs, _ in foods for ing in ingrs if ing not in bad))
