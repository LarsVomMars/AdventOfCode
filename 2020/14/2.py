def apply_mask(num: str, mask: str) -> str:
    new = ""
    for j in range(len(mask)):
        new += "1" if mask[j] == "1" else "0" if mask[j] == "0" else num[j]
    return new


def apply_addr_mask(addr: str, mask: str) -> list:
    l = [""]

    for j in range(len(mask)):
        if mask[j] == "1":
            for i in range(len(l)):
                l[i] += "1"
        elif mask[j] == "0":
            for i in range(len(l)):
                l[i] += addr[j]
        elif mask[j] == "X":
            for i in range(len(l)):
                l.append(l[i] + "1")
                l[i] += "0"

    return l


rows = open("input", "r").readlines()
rows = [row.strip() for row in rows]

mask = ""
mem = {}

for row in rows:
    if row.startswith("mask = "):
        mask = row[-36:]
        continue
    i = row[row.index("[")+1:row.index("]")]

    mis = apply_addr_mask(format(int(i), "036b"), mask)

    num = int(row.split("=")[1])

    for j in mis:
        mem[int(j, 2)] = num

print(sum(mem.values()))
