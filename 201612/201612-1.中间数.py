n = int(input())
s = input().split()
nums = [int(t) for t in s]
nums.sort()
target = nums[n//2]
i, j = 0, 0
for num in nums:
    if num < target:
        i += 1
    elif num > target:
        j += 1
if i == j:
    print(target)
else:
    print(-1)
