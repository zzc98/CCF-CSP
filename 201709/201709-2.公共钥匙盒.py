string = input().split()
N, K = int(string[0]), int(string[1])
keys = [i for i in range(1, N+1)]
borrow, repay = list(), list()
borrow_num, repay_num = K, K
for _ in range(K):
    s = input().split()
    borrow.append((int(s[1]), int(s[0])))  # start_time, id
    repay.append((int(s[1]) + int(s[2]), int(s[0])))  # end_time, id
borrow.sort()
repay.sort()
while borrow_num > 0:
    b, r = borrow[0], repay[0]
    if b[0] < r[0]:  # 借钥匙
        for i in range(N):
            if keys[i] == b[1]:
                keys[i] = 0
                break
        borrow.pop(0)
        borrow_num -= 1
    else:  # 还钥匙
        for i in range(N):
            if keys[i] == 0:
                keys[i] = r[1]
                break
        repay.pop(0)
        repay_num -= 1

while repay_num > 0:
    r = repay.pop(0)
    for i in range(N):
        if keys[i] == 0:
            keys[i] = r[1]
            break
    repay_num -= 1

for k in keys:
    print(k, end=' ')

"""
5 7
1 1 14
3 3 12
1 15 12
2 7 20
3 18 12
4 21 19
5 30 9
---------
1 2 3 5 4

"""