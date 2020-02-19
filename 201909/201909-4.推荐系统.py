"""
运行超时，20分
"""import heapq
s = input().split()
m, n = int(s[0]), int(s[1])  # m是类别数目，n是商品数目
categorys = []  # pid
categorysort = []  # (score, pid)
t1 = set()
t2 = list()
for _ in range(n):  # 初始化n个商品
    s = input().split()
    pid, score = int(s[0]), int(s[1]) * (-1)
    t1.add(pid)
    t2.append((score, pid))
t2.sort()
for i in range(m):
    categorys.append(t1.copy())
    categorysort.append(t2.copy())
opnum = int(input())
ans = []
for _ in range(opnum):
    s = input().split()
    if s[0] == '1':
        cid, pid, score = int(s[1]), int(s[2]), int(s[3]) * (-1)
        categorys[cid].add(pid)
        heapq.heappush(categorysort[cid], (score, pid))
    elif s[0] == '2':
        cid, pid = int(s[1]), int(s[2])
        categorys[cid].remove(pid)
    else:
        k0 = int(s[1])
        limitnum = []
        for i in range(2, m+2):
            limitnum.append(int(s[i]))
        temp = []
        for cid in range(m):
            num = limitnum[cid]
            i = 0
            for item in categorysort[cid]:
                if i >= num:
                    break
                if item[1] in categorys[cid]:
                    temp.append((item[0], cid, item[1]))  # score, cid, pid
                    i += 1
        temp.sort()
        a = [[] for i in range(m)]
        i = 0
        for item in temp:
            if i == k0:
                break
            i += 1
            cid, pid = item[1], item[2]
            a[cid].append(pid)
        for i in a:
            if len(i) == 0:
                i.append(-1)
        ans.append(a)
for ask in ans:
    for i in ask:
        for j in i:
            print(j, end=' ')
        print()


"""
2 3
1 3
2 2
3 1
8
3 100 1 1
1 0 4 3
1 0 5 1
3 10 2 2
3 10 1 1
2 0 1
3 2 1 1
3 1 1 1


1
1
1 4
1 2
1
1
4
1
4
-1
"""
