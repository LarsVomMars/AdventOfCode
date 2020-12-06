rows = open("input", "r").read()

groups = rows.split("\n\n")

s = 0

for group in groups:
    filtered = "".join(group.splitlines())  # Generate one line of chars
    cnt = len(group.splitlines())
    cd = {}
    for c in filtered:
        if c in cd:
            cd[c] += 1
        else:
            cd[c] = 1

    s += sum([1 if cd[c] == cnt else 0 for c in cd])

print(s)
