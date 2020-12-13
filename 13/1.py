rows = open("input", "r").readlines()
dep = int(rows[0])
times = list(filter(lambda x: x > 0, [int(row) if row != "x" else 0 for row in rows[1].split(",")]))

print(dep, times)

smallest = None
sid = -1

for dt in times:
    rem = dt - (dep % dt)
    if smallest is None or rem < smallest:
        smallest = rem
        sid = dt

print(smallest * sid)



