rows = open("input", "r").readlines()
rows = [row.strip() for row in rows]

mask = ""
mem = {}

for row in rows:
    if row.startswith("mask = "):
        mask = row[-36:]
        continue
    i = row[row.index("[") + 1:row.index("]")]
    num = format(int(row.split("=")[1]), "036b")
    new = ""
    for j in range(len(mask)):
        new += "1" if mask[j] == "1" else "0" if mask[j] == "0" else num[j]
    mem[i] = int(new, 2)

print(sum(mem.values()))
