import itertools
s1 = input().split()
N, M, K = int(s1[0]), int(s1[1]), int(s1[2])  # 节点数、重要数、需要数
s2 = input().split()
important = [int(t) for t in s2]

neighbor_dict = {}  # 嵌套字典
for i in range(N-1):
    s = input().split()
    u, v, w = int(s[0]), int(s[1]), int(s[2])
    if u in neighbor_dict:
        neighbor_dict[u][v] = w
    else:
        neighbor_dict[u] = dict()
        neighbor_dict[u][v] = w
    if v in neighbor_dict:
        neighbor_dict[v][u] = w
    else:
        neighbor_dict[v] = dict()
        neighbor_dict[v][u] = w

for start in important:
    queue = [(start, 0)]
    visited = {start}
    while len(queue) != 0:
        head = queue.pop(0)
        point, length = head[0], head[1]
        for neighbor in neighbor_dict[point]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, neighbor_dict[point][neighbor]+length))
            neighbor_dict[start][neighbor] = neighbor_dict[point][neighbor] + length


def getlength(points):
    res = 0
    for i in range(K):
        for j in range(i+1, K):
            res += neighbor_dict[points[i]][points[j]]
    return res


group = itertools.combinations_with_replacement(important, K)
ans = float("INF")
for option in group:
    if len(option) == len(set(option)):
        weight = getlength(option)
        ans = ans if ans < weight else weight

print(ans)


"""
5 3 2
1 3 5
1 2 4
1 3 5
1 4 3
4 5 1

4
"""
