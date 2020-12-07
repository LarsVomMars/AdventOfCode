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


def ctr(idx: str, specs: dict) -> int:
    if specs[idx] is None:
        return 0
    s = 0
    for spec in specs[idx].split(","):
        n = int(spec[0])
        spec = spec[1:]
        s += n + n * ctr(spec, specs)
    return s

print(ctr("shinygold", specs))