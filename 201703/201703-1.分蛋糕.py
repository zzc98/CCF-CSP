s = input().split()
n, k = int(s[0]), int(s[1])
s = input().split()
cakes = [int(t) for t in s]
num = 0
have = 0
for cake in cakes:
    have += cake
    if have >= k:
        num += 1
        have = 0
if have > 0:
    num += 1
print(num)
