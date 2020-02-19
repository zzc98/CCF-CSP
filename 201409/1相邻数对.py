n = int(input())
string = input().split()
num = [int(s) for s in string]
num.sort()
ans = 0
for i in range(1, n):
    if num[i] - num[i-1] == 1:
        ans += 1
print(ans)
