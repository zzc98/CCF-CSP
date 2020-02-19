s=input().split()
r, y, g = int(s[0]), int(s[1]), int(s[2])
n = int(input())

total = 0
for i in range(n):
    s = input().split()
    k, t = int(s[0]),int(s[1])
    if k == 0:
        total += t
    if k == 1:
        total += t
    if k == 3:
        total += 0
    if k == 2:
        total += t
        total += r

print(total)

"""
30 3 30
8
0 10
1 5
0 11
2 2
0 6
0 3
3 10
0 3

答案：70
"""
