rows = [row.strip() for row in open("input", "r").readlines()]

specs = {}

for row in rows:
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


def ctr(idx: str) -> int:
    if specs[idx] is None:
        return 0
    s = 0
    for spec in specs[idx].split(","):
        n = int(spec[0])
        spec = spec[1:]
        s += n + n * ctr(spec)
    return s


print("1:", sum([has_gold(spec, specs.copy()) for spec in specs]))
print("2:", ctr("shinygold"))
