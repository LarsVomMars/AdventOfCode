rows = open("input", "r").readlines()

correct = 0

for row in rows:
    cond, pwd = row.split(": ")
    nums, char = cond.split()
    n1, n2 = nums.split("-")

    if int(n1) <= pwd.count(char) <= int(n2):
        print(row)
        correct += 1

print(correct)
