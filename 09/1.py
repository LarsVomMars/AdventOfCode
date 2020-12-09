rows = open("input", "r").readlines()
rows = list(map(int, rows))

for i in range(25, len(rows)):
    row = rows[i]
    preamble = rows[i-25:i+1]

    b = False
    for p in preamble:
        for o in preamble:
            if o + p == row and not o == p:
                b = True
                break
        if b:
            break
    
    if not b:
        print(row)
        break