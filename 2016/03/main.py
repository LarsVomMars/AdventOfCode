rows = [list(map(int, row.split())) for row in open("input").readlines()]

def p1(row):
    return row[0] + row[1] > row[2] and row[1] + row[2] > row[0] and row[0] + row[2] > row[1]


def p2(rows):
    ctr = 0
    for c in range(3):
        for r in range(0, len(rows), 3):
            ctr += p1([rows[r][c], rows[r+1][c], rows[r+2][c]])
    return ctr


print("1:", sum(map(p1, rows)))
print("2:", p2(rows))
