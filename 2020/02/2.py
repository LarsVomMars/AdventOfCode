rows = open("input", "r").readlines()

correct = 0

for row in rows:
    cond, pwd = row.split(": ")
    nums, char = cond.split()
    n1, n2 = nums.split("-")
    n1 = int(n1)
    n2 = int(n2)

    if (pwd[n1 - 1] == char and pwd[n2 - 1] != char) or (pwd[n1 - 1] != char and pwd[n2 - 1] == char):
        print(row)
        correct += 1

print(correct)
