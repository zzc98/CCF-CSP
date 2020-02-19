# 70分
n = int(input())
now_dir = input().split('/')[1:]  # 去掉 '/' 根路径
ans = []
for _ in range(n):
    string = input()
    if not string:
        ans.append(now_dir.copy())
        continue
    string = string.split('/')
    length = len(string)
    if string[0] == '':  # 说明是以 '/' 开头的
        res = list()
    elif string[0] == '..':  # 上一级路径，直接拼接之前的正规化的路径，再去掉最后一层
        res = now_dir.copy()
        res.pop(-1)
    elif string[0] == '.':  # 当前路径，直接拼接之前的正规化的路径
        res = now_dir.copy()
    else:  # 当前路径，直接拼接之前的正规化的路径
        res = now_dir.copy()
        string.insert(0, '.')
    for i in range(1, length):
        if not string[i] or string[i] == '.':
            continue
        elif string[i] == '..':
            try:
                res.pop(-1)
            except:
                res = list()
        else:
            res.append(string[i])
    ans.append(res)
for res in ans:
    temp = ''
    for a in res:
        temp = temp + '/' + a
    if not temp:
        temp = '/'
    print(temp)
