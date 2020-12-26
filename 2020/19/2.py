rule_data, data = open("input", "r").read().split("\n\n")

rule_data = [row.strip() for row in rule_data.splitlines()]
data = [row.strip() for row in data.splitlines()]

RULES = {}

for rule in rule_data:
    num, rule = rule.split(": ")
    prl = []
    if rule.startswith('"'):
        prl = rule[1]
    else:
        prl = [rule_set.split() for rule_set in rule.split(" | ")]
    RULES[num] = prl


def match_str(msg: str, rule: str = "0"):
    rsets = RULES[rule]
    if isinstance(rsets, str):
        if msg.startswith(rsets):
            yield msg[len(rsets):]
        return

    for rs in rsets:
        msgs = [msg]
        nmsgs = []
        for rule in rs:
            for m in msgs:
                nmsgs.extend(match_str(m, rule))
            msgs = nmsgs.copy()
            nmsgs = []
        yield from msgs  # Python generators in a nutshell


RULES["8"] = [["42"], ["42", "8"]]
RULES["11"] = [["42", "31"], ["42", "11", "31"]]

s = 0
for msg in data:
    if any(match == "" for match in match_str(msg)):
        s += 1
print(s)
