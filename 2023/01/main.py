import re

LINES = [line.strip() for line in open("input").readlines()]

reg_p1 = re.compile(r"\d")
reg_p2 = re.compile(r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))")

conv = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def p1():
    return sum(
        [int(nums[0] + nums[-1]) for line in LINES if (nums := reg_p1.findall(line))]
    )


def map_nums(nums):
    return [num if len(num) == 1 else str(conv.index(num)) for num in nums]


def p2():
    return sum(
        [
            int(nums[0] + nums[-1])
            for line in LINES
            if (nums := map_nums(reg_p2.findall(line)))
        ]
    )


print("1:", p1())
print("2:", p2())
