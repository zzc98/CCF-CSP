string = input().split()
n, m = int(string[0]), int(string[1])
graph = list()
for _ in range(n+1):
    t = [float('INF')]*(n+1)
    graph.append(t)
for _ in range(m):
    string = input().split()
    u, v, w = int(string[0]), int(string[1]), int(string[2])
    graph[u][v] = w
    graph[v][u] = w

total = 0
dist, parent = dict(), dict()
for i in range(2, n+1):
    dist[i] = graph[1][i]
    parent[i] = 1
for _ in range(n-1):
    min_dist, min_index = float('INF'), 1
    min_add = float('INF')
    for key in dist:  # 先找其中最小值，之后更新
        if dist[key] < min_dist:
            min_dist = dist[key]
            min_index = key
            if graph[parent[min_index]][min_index] < min_add:
                min_add = graph[parent[min_index]][min_index]
    total += min_add  # total增加
    del dist[min_index]
    for key in dist:
        temp = min_dist + graph[min_index][key]
        if temp <= dist[key]:
            parent[key] = min_index
            dist[key] = temp

print(total)
