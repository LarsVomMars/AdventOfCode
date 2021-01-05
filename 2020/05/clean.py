seats = sorted({int(row, 2) for row in
                open("input", "r").read()
               .replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
               .split("\n")[:-1]
                })

print("1:", seats[-1])
for seat in seats:
    if seat + 1 not in seats and seat + 2 in seats:
        print("2:", seat + 1)
        break
