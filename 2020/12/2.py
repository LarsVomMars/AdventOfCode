rows = open("input", "r").readlines()

pos = [0, 0]
wp = [1, 10]

for row in rows:
    mv = row[0]
    p = int(row[1:])

    if mv == "N":
        wp[0] += p
    elif mv == "S":
        wp[0] -= p
    elif mv == "E":
        wp[1] += p
    elif mv == "W":
        wp[1] -= p
    elif mv == "F": # Move ship by waypoint magnitude
        pos[0] += wp[0] * p
        pos[1] += wp[1] * p
    elif mv == "L": # Rotating the waypoint works the same
        l = p // 90
        for i in range(l):
            wp[0], wp[1] = wp[1], -wp[0]
    elif mv == "R":
        l = p // 90
        for i in range(l):
            wp[1], wp[0] = wp[0], -wp[1]

print(abs(pos[0]) + abs(pos[1]))
