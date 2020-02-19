n = int(input())
s = input().split()
nums = [int(t) for t in s]
ans = 0
po = set()  # 正数集合
for num in nums:
    if num > 0:
        po.add(num)
for num in nums:
    if num < 0:
        if num * (-1) in po:
            ans += 1
print(ans)