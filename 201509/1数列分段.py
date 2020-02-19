n = int(input())
s = input().split()
num = [int(i) for i in s]
ans = 1
last = num[0]
for i in range(1, n):
    if num[i] != last:
        last = num[i]
        ans += 1
print(ans)
