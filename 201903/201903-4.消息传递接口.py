"""
最后运行超时，只得了80分
"""

if __name__ == "__main__":
    # part1 数据读入
    string = input().split()
    code_num, thread_num = int(string[0]), int(string[1])
    codes = []
    for i in range(code_num):
        temp = []
        for j in range(thread_num):
            temp.append(input().split())
        codes.append(temp)

    # part2 处理
    for threads in codes:
        doing = []  # 初始化当前正在执行的操作集合
        for i in range(thread_num):
            doing.append(threads[i].pop(0))
        unchange = False
        while not unchange:
            unchange = True
            i = 0
            flag = False  # 外层循环标志
            while i < thread_num:
                if doing[i] == 'N':  # 'N'是完成标志
                    i = i + 1
                    continue
                operation = doing[i]
                X = operation[0] # S 或者 R
                who = int(operation[1:]) # 线程i等待的另一个线程
                operation2 = doing[who]
                if operation2 == 'N':
                    flag = True
                    break
                X2 = operation2[0]
                who2 = int(operation2[1:])
                if X != X2 and who2 == i:
                    flag = True
                    unchange = False
                    try:
                        doing[i] = threads[i].pop(0)
                    except:
                        doing[i] = 'N'
                    try:
                        doing[who] = threads[who].pop(0)
                    except:
                        doing[who] = 'N'
                    break
                if flag:
                    break
                else:
                    i = i + 1
        # 打印结果
        lock = False
        for i in doing:
            if i != 'N':
                lock = True
                break
        if lock:
            print(1)
        else:
            print(0)
