n = int(input())
string = input().split()
nums = [int(s) for s in string]
res = 0
for i in range(1, n-1):
    if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
        res += 1
    elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        res += 1
print(res)
