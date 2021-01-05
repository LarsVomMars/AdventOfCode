f = open("input", "r").read()

passes = f.split("\n\n")  # Split blanks

ps = []

reqProps = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

correct = 0

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
        correct += 1

print(correct)
