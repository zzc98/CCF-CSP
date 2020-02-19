"""
最后运行超时，只得了50分
"""
n = int(input())  # 节点数
m = int(input())  # 边数
input()
edge = [()] * m
for i in range(m):
    s = input().split()
    edge[i] = (int(s[2]), s[1], s[0])  # 边长，节点1，节点2

edge.sort(key=lambda item: item[0])  # 边按照长度排序
tree = dict() # 哪条边在哪棵树中
num = 0
for item in edge:
    v1, v2 = item[1], item[2]
    s1, s2 = v1 not in tree, v2 not in tree
    if s1 and s2:
        num += 1
        tree[v1] = num
        tree[v2] = num
    elif s2:
        num += 1
        tree[v2] = tree[v1]
    elif s1:
        num += 1
        tree[v1] = tree[v2]
    else:
        if tree[v1] == tree[v2]:
            continue
        else:
            num += 1
            if num == n - 1:
                print(item[0])
                break
            t = tree[v1]
            for key in tree:
                if tree[key] == t:
                    tree[key] = tree[v2]
    if num == n - 1:
        print(item[0])
        break
