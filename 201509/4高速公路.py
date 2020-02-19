def dfs(u):
    visit1.append(u)
    for v in g1[u]:
        if v not in visit1:
            dfs(v)
    black.append(u)


def dfs2(u):
    visit2.append(u)
    for v in g2[u]:
        if v not in visit2:
            dfs2(v)


s = input().split()
n, m = int(s[0]), int(s[1])
g1 = [list() for _ in range(n+1)]
g2 = [list() for _ in range(n+1)]
for _ in range(m):
    s = input().split()
    u, v = int(s[0]), int(s[1])
    g1[u].append(v)
    g2[v].append(u)

visit1 = []
black = []
for i in range(1, n+1):
    if i not in visit1:
        dfs(i)

ans = 0
visit2 = []
for _ in range(n):
    t = black.pop(-1)
    if t not in visit2:
        start = len(visit2)
        dfs2(t)
        end = len(visit2) - start
        ans += end * (end-1) / 2
print(int(ans))
