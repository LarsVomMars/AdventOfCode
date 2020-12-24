FILLER = int(1e6)
ROUNDS = int(1e7)
NUM_STR = "496138527"

nums = list(map(lambda x: int(x) - 1, list(NUM_STR)))
nums += list(range(max(nums) + 1, FILLER))
nx_nums = [None for _ in nums]
mx = max(nums) + 1

for z1, z2 in zip(nums, nums[1:] + nums[:1]):
    nx_nums[z1] = z2

cn = nums[0]
for _ in range(ROUNDS):
    prev = cn
    cn = nx_nums[cn]
    vals = [cn] + [cn := nx_nums[cn] for _ in range(2)]
    cn = nx_nums[cn]
    nx_nums[prev] = cn
    dest = prev
    while dest in [*vals, prev]:
        dest = (dest - 1 + mx) % mx
    vals = [dest, *vals, nx_nums[dest]]
    for a, b in zip(vals, vals[1:]):
        nx_nums[a] = b

print((nx_nums[0] + 1) * (nx_nums[nx_nums[0]] + 1))
