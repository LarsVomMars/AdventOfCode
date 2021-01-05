rows = open("input.txt", "r").readlines()
rows = list(map(int, rows))

small = []
large = []

for num in rows:
    if num < 1000:
        small.append(num)
    else:
        large.append(num)

for n in small:
    r = 2020 - n
    for l in large:
        if l == r:
            print(n, l, l * n)
