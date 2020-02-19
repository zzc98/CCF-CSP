if __name__ == "__main__":
    tree = int(input())
    total = 0
    drop = [False] * tree
    for i in range(tree):
        op = input().split()
        length = int(op[0]) + 1
        cur_num = int(op[1])
        j = 2
        while j < length:
            read = int(op[j])
            if read <= 0:
                cur_num += read
            elif cur_num > read:
                    drop[i] = True
                    cur_num = read
            j += 1
        total += cur_num
    e = 0
    if tree < 3:
        e = 0
    elif tree == 3:
        e = 3 if drop[0] and drop[1] and drop[2] else 0
    else:
        i = 2
        po = tree-1
        while i < po:
            if drop[i-1] and drop[i] and drop[i+1]:
                e += 1
            i += 1
        if drop[-1] and drop[0] and drop[1]:
            e += 1
        if drop[-2] and drop[-1] and drop[0]:
            e += 1
    print(total, sum(drop), e)


"""
4
4 74 -7 -12 -5
5 73 -8 -6 59 -4
5 76 -5 -10 60 -2
5 80 -6 -15 59 0

结果：222 1 0

5
4 10 0 9 0
4 10 -2 7 0
2 10 0
4 10 -3 5 0
4 10 -1 8 0

结果：39 4 2
"""