from collections import defaultdict

parts = open("input").read().split("\n\n")

RULES = defaultdict(list)
for line in parts[0].splitlines():
    prev, next = line.split("|")
    RULES[int(prev)].append(int(next))

UPDATES = [list(map(int, line.strip().split(","))) for line in parts[1].splitlines()]

def all():
    s1 = 0
    s2 = 0
    for update in UPDATES:
        incorrect = False
        while True:
            for i, num in enumerate(update):
                rule = RULES[num]
                for r in rule:
                    if r in update[:i]:
                        incorrect = True
                        update[i], update[update.index(r)] = update[update.index(r)], update[i]
                        break
                else:
                    continue
                break
            else:
                if incorrect:
                    s2 += update[len(update) // 2]
                else:
                    s1 += update[len(update) // 2]
                break
    return s1, s2

p1, p2 = all()

print("1:", p1)
print("2:", p2)
