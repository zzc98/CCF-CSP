"""
暴力法求解，20分
"""

U = [314882150829468584, 427197303358170108, 1022292690726729920,
     1698479428772363217, 2006101093849356424]


def f(x):
    t = x % 2009731336725594113
    return t % 2019


s = input().split()
n, q = int(s[0]), int(s[1])
A = [i for i in range(n+1)]
F = []
for a in A:
    F.append(f(a))

ans = []
for _ in range(q):
    s = input().split()
    l, r = int(s[0]), int(s[1])
    s = 0
    for i in range(l, r+1):
        s += F[i]
    ans.append(s)
    t = s % 5
    for i in range(l, r+1):
        A[i] = A[i] * U[t]
        F[i] = f(A[i])

for a in ans:
    print(a)

"""
4 4
1 3
3 4
3 3
1 3


6
1105
1735
4744
"""