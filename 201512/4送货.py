def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    t = [0] * (n+1)
    graph = []
    for _ in range(n+1):
        graph.append(t.copy())
    for _ in range(m):
        s = input().split()
        u, v = int(s[0]), int(s[1])
        graph[u][v], graph[v][u] = 1, 1

    def dfs(p):
        if len(ans) == m:
            return True
        for j in range(1, n+1):
            if graph[p][j] == 1 and (p, j) not in ans and (j, p) not in ans:  # 边存在，而且没遍历过
                ans.append((p, j))
                if dfs(j):
                    return True
                else:
                    ans.pop(-1)
        return False

    for i in range(1, n+1):
        ans = []
        if dfs(i):
            for a in ans:
                print(a[0], end=' ')
            print(ans[-1][1])
            return
    print(-1)


if __name__ == "__main__":
    main()
