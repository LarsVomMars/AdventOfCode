rows = open("input", "r").readlines()

face = [0, 1]
pos = [0, 0]

for row in rows:
    mv = row[0]
    p = int(row[1:])

    if mv == "N":
        pos[0] += p
    elif mv == "S":
        pos[0] -= p
    elif mv == "E":
        pos[1] += p
    elif mv == "W":
        pos[1] -= p
    elif mv == "F":
        pos[0] += face[0] * p
        pos[1] += face[1] * p
    elif mv == "L":
        l = p // 90
        for i in range(l):
            face[0], face[1] = face[1], -face[0]
    elif mv == "R":
        l = p // 90
        for i in range(l):
            face[1], face[0] = face[0], -face[1]

print(abs(pos[0]) + abs(pos[1]))
