rows = open("input.txt", "r").readlines()
rows = list(map(int, rows))

for i in rows:
    for j in rows:
        for k in rows:
            if i + j + k == 2020:
                print(i, j, k, i*j*k)