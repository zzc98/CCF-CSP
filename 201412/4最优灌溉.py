s = input().split()
n, m = int(s[0]), int(s[1])
edges = []
for _ in range(m):
    s = input().split()
    u, v, w = int(s[0]), int(s[1]), int(s[2])
    edges.append((w, u, v))
edges.sort()
tree = dict()
for i in range(1, n+1):
    tree[i] = i
ans = 0
for edge in edges:
    w, u, v = edge[0], edge[1], edge[2]
    if tree[u] == tree[v]:
        continue
    else:
        target = tree[v]
        for k in tree:
            if tree[k] == target:
                tree[k] = tree[u]
        ans += w
print(ans)
