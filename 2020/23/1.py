nums = list(map(int, list("496138527")))

for _ in range(100):
    n = nums.pop(0)
    mv = nums[:3]
    del nums[:3]
    mx = max(nums)
    mn = min(nums)
    c = n - 1
    while c not in nums:
        c = c - 1 if c - 1 >= mn else mx
    ni = nums.index(c)
    nums[ni + 1:ni + 1] = mv
    nums.append(n)

oi = nums.index(1)
print("".join(map(str, (nums[oi + 1:] + nums[:oi]))))
