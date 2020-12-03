rows = open("input", "r").readlines()

def search(rows, right: int = 3, down: int = 1) -> int:
    trees = 0
    left = 0
    CHAR_T = "#"

    for i in range(0, len(rows), down):
        row = rows[i].strip()
        if row[left] == CHAR_T:
            trees += 1
        
        left = (left + right) % len(row)

    return trees

print(search(rows))