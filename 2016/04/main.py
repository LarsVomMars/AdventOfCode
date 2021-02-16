rows = [row.strip() for row in open("input").readlines()]

def p1(row):
    chars = "".join(row.split("-"))
    ctr_dict = {}
    for c in chars:
        if c.isdigit(): break
        if c in ctr_dict:
            ctr_dict[c] += 1
        else:
            ctr_dict[c]
