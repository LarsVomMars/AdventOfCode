rows = open("input", "r").read()

groups = rows.split("\n\n")

s = 0

for group in groups:
    filtered = "".join(set("".join(group.splitlines())))
    s += len(filtered)

print(s)

# Wohooo
print(sum([len("".join(set("".join(group.splitlines())))) for group in groups]))