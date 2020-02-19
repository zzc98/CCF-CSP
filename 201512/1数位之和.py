s = input()
length = len(s)
ans = 0
for i in range(length):
    ans += int(s[i])
print(ans)