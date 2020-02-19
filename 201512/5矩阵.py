dim = int(input())


def mv(m, v):
    res = []
    for i in range(dim):
        t = 0
        for j in range(dim):
            if m[i][j] == 1 and v[j] == 1:
                t += 1
        res.append(t % 2)
    return res


def mm(m1, m2):
    res = []
    for i in range(dim):
        t = []
        for j in range(dim):
            q = 0
            for k in range(dim):
                if m1[i][k] == 1 and m2[k][j] == 1:
                    q += 1
            t.append(q % 2)
        res.append(t)
    return res


def gen(num):
    if num % 2 == 0:
        m = num//2
        if m not in dic:
            gen(m)
        dic[num] = mm(dic[m], dic[m])
    else:
        m1, m2 = num//2, num // 2 + 1
        if m1 not in dic:
            gen(m1)
        if m2 not in dic:
            gen(m2)
        dic[num] = mm(dic[m1], dic[m2])


A = []  # 初始化矩阵
for _ in range(dim):
    s = input()
    t = [int(i) for i in s]
    A.append(t)
s = input()
b = [int(i) for i in s]  # 初始化向量
dic = {0: 0, 1: A}
times = []
s = int(input())
for _ in range(s):
    time = int(input())
    times.append(time)
    if time not in dic:
        gen(time)

for i in times:
    if i == 0:
        for j in b:
            print(j, end='')
        print()
        continue
    s = mv(dic[i], b)
    for j in s:
        print(j, end='')
    print()
