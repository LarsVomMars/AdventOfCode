LINES = [list(map(int, line.strip().split())) for line in open("input").readlines()]


def get_last(line):
    if all(x == 0 for x in line):
        return (0, 0)
    new_line = [b - a for a, b in zip(line, line[1:])]
    ends = get_last(new_line)
    return (line[0] - ends[0], line[-1] + ends[1])


b, a = (sum(nums) for nums in zip(*[get_last(line) for line in LINES]))

print("1:", a)
print("2:", b)
