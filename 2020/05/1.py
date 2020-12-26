rows = open("input", "r").readlines()

sids = []

for row in rows:
    row = row.strip()

    # row = "FBFBBFFRLR"
    srow = row[:7]
    seat = row[7:]

    b = 0
    t = 127
    for rc in srow:
        d = ((t - b) // 2) +1
        if rc == "F":
            t -= d
        elif rc == "B":
            b += d

    nrow = b

    b = 0
    t = 7
    for rc in seat:
        d = ((t - b) // 2) +1
        if rc == "L":
            t -= d
        elif rc == "R":
            b += d


    nseat = b

    sids.append(nrow * 8 + nseat)

print(max(sids))
            
    