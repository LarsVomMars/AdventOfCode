instructions = open("input", "r").read().strip()

print("1:", instructions.count("(") - instructions.count(")"))

floor = 0
for i, c in enumerate(instructions):
    if (floor := floor + (1 if c == "(" else -1)) == -1:
        print("2:", i+1)
        break
