string = input().split()
n, m = int(string[0]),  int(string[1])
string = input().split()
nums = [int(s) for s in string]
nums.insert(0, 0)
ans = []
for _ in range(m):
    s = input().split()
    if s[0] == '1':
        v = int(s[3])
        for i in range(int(s[1]), int(s[2])+1):
            if nums[i] % v == 0:
                nums[i] = nums[i]//v
    else:
        total = 0
        for i in range(int(s[1]), int(s[2])+1):
            total += nums[i]
        ans.append(total)
for a in ans:
    print(a)
