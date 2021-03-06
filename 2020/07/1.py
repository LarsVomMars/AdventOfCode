rows = open("input", "r").readlines()

specs = {}

for row in rows:
    row = row.strip()
    sbag = "".join(row.split()[:2])
    if row.endswith("no other bags."):
        specs[sbag] = None
    else:
        bag_spec = "".join(row.split()[4:])[:-1].replace("bags", "").replace("bag", "")
        specs[sbag] = bag_spec


def has_gold(idx: str, specs: dict) -> bool:
    if specs[idx] is None or specs[idx] == "":
        return False
    elif "shinygold" in specs[idx]:
        return True
    else:
        for i in specs[idx].split(","):
            if not has_gold(i[1:], specs):
                specs[idx] = specs[idx].replace(f"{i},", "").replace(i, "")
            else:
                return True
        return False


hg = 0
for spec in specs:
    hg += 1 if has_gold(spec, specs) else 0

print(hg)
