LINES = [list((l.strip() for l in line.split("|")))
         for line in open("input").readlines()]


def p1():
    return sum(sum(len(cl) in [2, 3, 4, 7] for cl in l[1].split()) for l in LINES)


def p2():
    sm = 0
    for line in LINES:
        posses = list(map(set, line[0].split()))

        # Get bases
        one = next(filter(lambda x: len(x) == 2, posses))
        four = next(filter(lambda x: len(x) == 4, posses))
        seven = next(filter(lambda x: len(x) == 3, posses))
        eight = next(filter(lambda x: len(x) == 7, posses))

        # 6 digits
        nine = next(filter(lambda x: len(x) ==
                           6 and len(x & four) == 4, posses))
        zero = next(filter(lambda x: len(x) == 6 and len(
            x & seven) == 3 and x != nine, posses))
        six = next(filter(lambda x: len(x) ==
                          6 and x not in [zero, nine], posses))

        # 5 digits
        five = next(filter(lambda x: len(x) ==
                           5 and len(x & six) == 5, posses))
        three = next(filter(lambda x: len(x) == 5 and len(
            x & four) == 3 and x != five, posses))
        two = next(filter(lambda x: len(x) ==
                          5 and x not in [three, five], posses))

        nums = (zero, one, two, three, four, five, six, seven, eight, nine)

        for i, num in enumerate(line[1].split()):
            idx = nums.index(set(num))
            sm += idx * 10 ** (3 - i)

    return sm


print("1:", p1())
print("2:", p2())
