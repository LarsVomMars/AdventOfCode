from itertools import product

rule_data, data = open("input", "r").read().split("\n\n")

rule_data = [row.strip() for row in rule_data.splitlines()]
data = [row.strip() for row in data.splitlines()]

RULES = {}
for rule in rule_data:
    num, rule = rule.split(": ")
    RULES[int(num)] = rule


def solve(idx: int = 0):
    if '"' in RULES[idx]:
        yield RULES[idx][1]
    else:
        for or_part in RULES[idx].split(" | "):  # Use in RULES init
            for part in product(*[list(solve(int(num))) for num in or_part.split()]):
                yield "".join(part)


valid = list(solve())
s = 0
for msg in data:
    if msg in valid:
        print(msg)
        s += 1

print(s)
