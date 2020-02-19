string = input().split()
m, n, q = int(string[0]), int(string[1]), int(string[2])
game = [] # 画布
t = ['.' for _ in range(m)]  # m 是宽度 列数 x
for _ in range(n):  # n 是高度 行数 y
    game.append(t.copy())
change = n - 1
for _ in range(q):
    s = input().split()
    if s[0] == '0':  # 画线
        x1, y1, x2, y2 = int(s[1]), change - \
            int(s[2]), int(s[3]), change - int(s[4])
        if x1 == x2:  # 画 |
            if y1 > y2:  # 保证，y1 在上，y2在下
                y1, y2 = y2, y1
            for j in range(y1, y2+1):
                if game[j][x1] == '-':
                    game[j][x1] = '+'
                elif game[j][x1] == '+':
                    continue
                else:
                    game[j][x1] = '|'
        else:  # 画 -
            if x1 > x2:  # 保证，x1 在左，x2在右
                x1, x2 = x2, x1
            for j in range(x1, x2+1):
                if game[y1][j] == '|':
                    game[y1][j] = '+'
                elif game[y1][j] == '+':
                    continue
                else:
                    game[y1][j] = '-'
    else:  # 填充
        x, y, c = int(s[1]), change - int(s[2]), s[3]
        # BFS
        stop = {'-', '|', '+', c}
        queue = [(x, y)]
        q_len = 1
        game[y][x] = c
        while q_len != 0:
            head = queue.pop(0)
            q_len -= 1
            # 上(x, y-1)
            z = head[1] - 1
            if z >= 0 and game[z][head[0]] not in stop:
                game[z][head[0]] = c
                queue.append((head[0], z))
                q_len += 1
            # 下(x, y+1)
            z = head[1] + 1
            if z < n and game[z][head[0]] not in stop:
                game[z][head[0]] = c
                queue.append((head[0], z))
                q_len += 1
            # 左(x-1, y)
            z = head[0] - 1
            if z >= 0 and game[head[1]][z] not in stop:
                game[head[1]][z] = c
                queue.append((z, head[1]))
                q_len += 1
            # 右(x+1, y)
            z = head[0] + 1
            if z < m and game[head[1]][z] not in stop:
                game[head[1]][z] = c
                queue.append((z, head[1]))
                q_len += 1
for r in game:
    for c in r:
        print(c, end='')
    print()

"""
16 13 9
0 3 1 12 1
0 12 1 12 3
0 12 3 6 3
0 6 3 6 9
0 6 9 12 9
0 12 9 12 11
0 12 11 3 11
0 3 11 3 1
1 4 2 C

"""
