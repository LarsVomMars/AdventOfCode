nums = [1,17,0,10,18,11,6]
BREAK_I = 30_000_000
idxs = {}
lnum = None

for i in range(BREAK_I):
    if i < len(nums):
        num = nums[i]
    else:
        num = 0 if lnum not in idxs else (i - 1) - idxs[lnum]
    idxs[lnum] = i - 1
    lnum = num
print(num)
