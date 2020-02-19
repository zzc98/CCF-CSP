# DFS 和 BFS都是60
# DFS
string = input().split()
n, m = int(string[0]),  int(string[1])
g1, g2 = [], []
for _ in range(n+1):
    g1.append([0] * (n+1))
    g2.append([0] * (n+1))

for _ in range(m):
    s = input().split()
    u, v = int(s[0]),  int(s[1])
    g1[u][v] = 1  # 发送消息图
    g2[v][u] = 1  # 接收消息图


def dfs(graph, visited, i):
    visited.add(i)
    for j in range(1, n+1):
        if j not in visited and graph[i][j] == 1:
            dfs(graph, visited, j)


ans = set()
for i in range(1, n+1):
    visited1 = set()
    visited2 = set()
    dfs(g1, visited1, i)
    dfs(g2, visited2, i)
    visited = visited1.union(visited2)
    if len(visited) == n:
        ans.add(i)

print(len(ans))

# BFS
string = input().split()
n, m = int(string[0]),  int(string[1])
g1, g2 = [], []
for _ in range(n+1):
    g1.append([0] * (n+1))
    g2.append([0] * (n+1))

for _ in range(m):
    s = input().split()
    u, v = int(s[0]),  int(s[1])
    g1[u][v] = 1  # 发送消息图
    g2[v][u] = 1  # 接收消息图


ans = list()
for i in range(1, n+1):
    q = [i]
    visited1 = {i}
    while len(q) != 0:
        head = q.pop(0)
        for j in range(1, n+1):
            if j not in visited1 and g1[head][j] == 1:
                q.append(j)
                visited1.add(j)
    q = [i]
    visited2 = {i}
    while len(q) != 0:
        head = q.pop(0)
        for j in range(1, n+1):
            if j not in visited2 and g2[head][j] == 1:
                q.append(j)
                visited2.add(j)
    visited = visited1.union(visited2)
    if len(visited) == n:
        ans.append(i)

print(len(ans))


"""
4 4
1 2
1 3
2 4
3 4
---
2
"""