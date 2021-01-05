nums = [1, 17, 0, 10, 18, 11, 6]

ctr = len(nums)
BREAK_I = 2020

while True:
    ln = nums[-1]
    cnt = nums.count(ln)
    if cnt == 1:
        nums.append(0)
    elif cnt > 1:
        i = len(nums) - nums[:-1][::-1].index(ln) - 1
        nums.append(len(nums) - i)

    if (ctr := ctr + 1) == BREAK_I: break
print(nums[-1])
