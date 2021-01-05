from string import hexdigits


def validateProps(props: dict) -> bool:
    for prop in props:
        pv = props[prop]
        if prop == "byr":
            if not (1920 <= int(pv) <= 2002):
                return False
        elif prop == "iyr":
            if not (2010 <= int(pv) <= 2020):
                return False
        elif prop == "eyr":
            if not (2020 <= int(pv) <= 2030):
                return False
        elif prop == "hgt":
            if pv.endswith("in"):
                v = int(pv[:-2])
                if not (59 <= v <= 76):
                    return False
            elif pv.endswith("cm"):
                v = int(pv[:-2])
                if not (150 <= v <= 193):
                    return False
            else:
                return False
        elif prop == "hcl":
            if not pv.startswith("#") or not len(pv) == 7 or not all(c in hexdigits for c in pv[1:]):
                return False
        elif prop == "ecl":
            if pv not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif prop == "pid":
            if not len(pv) == 9 or not pv.isdigit():
                return False
    return True


passes = open("input", "r").read().split("\n\n")

reqProps = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

p1 = 0
p2 = 0
for pazz in passes:
    rows = pazz.split("\n")  # Split rows in passes
    p = {}
    for row in rows:
        if len(row) == 0:
            continue
        props = row.split(" ")  # Split space
        for prop in props:
            pr, attr = prop.strip().split(":")
            p[pr] = attr

    props = p.keys()
    if all(rp in props for rp in reqProps):
        p1 += 1
        if validateProps(p):
            p2 += 1

print("1:", p1)
print("2:", p2)
