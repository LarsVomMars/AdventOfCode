rows = open("input", "r").readlines()
rows = list(map(int, rows))

N = 26796446 # Result from 1

for i in range(len(rows)):
    j = i
    s = 0
    while True:
        s += rows[j]
        if s >= N:
            break
        j += 1

    if s == N:
        r = rows[i:j+1]
        print(min(r)+max(r))
        break
