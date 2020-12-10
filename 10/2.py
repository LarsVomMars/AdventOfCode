rows = open("input", "r").readlines()
rows.append(0)  # Add outlet and device diffs
rows = sorted(list(map(int, rows)))
rows.append(rows[-1]+3)

res = [1]

for i in range(1, len(rows)):
    res.insert(i, res[i-1])
    if i - 2 >= 0 and (rows[i] - 2 == rows[i - 2] or rows[i] - 3 == rows[i - 2]):
        res[i] += res[i-2]
    if i - 3 >= 0 and (rows[i] - 3 == rows[i - 3]):
        res[i] += res[i-3]

print(res[-1])
