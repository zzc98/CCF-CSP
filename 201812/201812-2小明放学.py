s=input().split()
r, y, g = int(s[0]), int(s[1]), int(s[2])
n = int(input())

c = r + y + g # 一个周期
total = 0
now = 0 # 绝对偏移量

for i in range(n):
    s = input().split()
    k, t = int(s[0]),int(s[1])
    wait = 0
    if k == 0:
        wait = t
    else:
        if k == 1:
            pointer = y + r - t # 相对偏移量
        elif k == 2:
            pointer = y - t
        else:
            pointer = c - t

        pointer = now + pointer
        pointer = pointer % c
        if pointer >= y + r:
            wait = 0
        else:
            wait = y + r - pointer

    total += wait
    now += wait
    now = now % c

print(total)

"""
30 3 30
8
0 10
1 5
0 11
2 2
0 6
0 3
3 10
0 3

答案：46
"""
