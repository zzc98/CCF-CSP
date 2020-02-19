count = int(input())
ans = []
for i in range(count):
    string = input()
    string = string.replace('x', '*')
    string = string.replace('/', '//')
    a = eval(string)
    if a == 24:
        ans.append('Yes')
    else:
        ans.append('No')
for i in range(count):
    print(ans[i])

"""
10
9+3+4x3
5+4x5x5
7-9-9+8
5x6/5x4
3+5+7+9
1x1+9-9
1x9-5/9
8/5+6x9
6x7-3x6
6x4+4/5
"""
