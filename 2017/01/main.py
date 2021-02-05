nums = list(map(int, list(open("input", "r").read().strip())))


def p1(nums: list):
    nnums = nums.copy() + [nums[0]]
    s = sum(n for i, n in enumerate(nnums[:-1]) if n == nnums[i + 1])
    return s


def p2(nums: list):
    l = len(nums)
    print(l)
    return sum(n for i, n in enumerate(nums) if n == nums[(i + l // 2) % l])


print("1:", p1(nums))
print("2:", p2(nums))
