rows = open("input", "r").readlines()
rows.append(0) # Add outlet and device diffs
rows = sorted(list(map(int, rows)))
rows.append(rows[-1]+3)

s1 = 0
s3 = 0
for i in range(1, len(rows)):
    if rows[i] - 1 == rows[i-1]:
        s1 += 1
    elif rows[i] - 3 == rows[i-1]:
        s3 += 1

print(s1 * s3)
