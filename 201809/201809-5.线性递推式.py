Q = 998244353
s = input().split()
m, l, r = int(s[0]), int(s[1]), int(s[2])
s = input().split()
k = [int(t) for t in s]
a = [1]
for i in range(1, m):
    t = 0
    for j in range(i):
        t += k[j] * a[i-j-1]
    t = t % Q
    a.append(t)

for i in range(m, r+1):
    t = 0
    alen = len(a)
    for j in range(m):
        t += k[j]*a[alen-j-1]
    t = t % Q
    a.append(t)

for i in range(l, r+1):
    print(a[i])

"""
3 3 6
2 0 4

12
32
80
208


10 10 20
532737790 634932889 335818534 101179174 977780682 695192541 779962395 295668292 157661238 325351676
"""
