n = int(input())
string = input().split()
data = [int(s) for s in string]
ans = 0
for i in range(1, n):
    temp = abs(data[i] - data[i-1])
    if temp > ans:
        ans = temp
print(ans)
