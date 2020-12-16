ufields, uticket, unearby = open("input", "r").read().split("\n\n")

fields = []
for field in ufields.splitlines():
    f1, f2 = field.split(":")[1].split(" or ")
    f1 = list(map(int, f1.split("-")))
    f2 = list(map(int, f2.split("-")))
    f1 = list(range(f1[0], f1[1]+1))
    f2 = list(range(f2[0], f2[1]+1))
    fields += f1 + f2

fields = set(fields)

s = []
for nearby in unearby.splitlines()[1:]:
    ticket = list(map(int, nearby.split(",")))
    for val in ticket:
        if val not in fields:
            s.append(val)

print(sum(s))