seat = []
for i in range(20):
    t = [1]*5
    seat.append(t)
num = int(input())
string = input().split()
buy_num = [int(s) for s in string]
ans = []
for buy in buy_num:
    if buy == 1:  # 只购买一张
        flag = False
        for i in range(20):
            for j in range(5):
                if seat[i][j] == 1:
                    seat[i][j] = 0
                    ans.append([i*5+j+1])
                    flag = True
                    break
            if flag:
                break
    elif buy == 2:
        flag = False
        for i in range(20):
            for j in range(1, 5):
                if seat[i][j] == 1 and seat[i][j-1] == 1:
                    seat[i][j] = 0
                    seat[i][j-1] = 0
                    ans.append([i*5+j, i*5+j+1])
                    flag = True
                    break
            if flag:
                break
        # 没有连续的座位了
        if not flag:
            t = []
            for i in range(20):
                for j in range(5):
                    if seat[i][j] == 1:
                        seat[i][j] = 0
                        t.append(i*5+j+1)
                        if len(t) == 2:
                            ans.append(t)
                            flag = True
                            break
                if flag:
                    break
    elif buy == 3:
        flag = False
        for i in range(20):
            for j in range(2, 5):
                if seat[i][j] == 1 and seat[i][j-1] == 1 and seat[i][j-2] == 1:
                    seat[i][j] = 0
                    seat[i][j-1] = 0
                    seat[i][j-2] = 0
                    ans.append([i*5+j-1, i*5+j, i*5+j+1])
                    flag = True
                    break
            if flag:
                break
        # 没有连续的座位了
        if not flag:
            t = []
            for i in range(20):
                for j in range(5):
                    if seat[i][j] == 1:
                        seat[i][j] = 0
                        t.append(i*5+j+1)
                        if len(t) == 3:
                            ans.append(t)
                            flag = True
                            break
                if flag:
                    break
    elif buy == 4:
        flag = False
        for i in range(20):
            for j in range(3, 5):
                if seat[i][j] == 1 and seat[i][j-1] == 1 and seat[i][j-2] == 1 and seat[i][j-3] == 1:
                    seat[i][j] = 0
                    seat[i][j-1] = 0
                    seat[i][j-2] = 0
                    seat[i][j-3] = 0
                    ans.append([i*5+j-2, i*5+j-1, i*5+j, i*5+j+1])
                    flag = True
                    break
            if flag:
                break
        # 没有连续的座位了
        if not flag:
            t = []
            for i in range(20):
                for j in range(5):
                    if seat[i][j] == 1:
                        seat[i][j] = 0
                        t.append(i*5+j+1)
                        if len(t) == 4:
                            ans.append(t)
                            flag = True
                            break
                if flag:
                    break
    elif buy == 5:
        flag = False
        for i in range(20):
            if seat[i][0] == 1 and seat[i][1] == 1 and seat[i][2] == 1 and seat[i][3] == 1 and seat[i][4] == 1:
                seat[i][0] = 0
                seat[i][1] = 0
                seat[i][2] = 0
                seat[i][3] = 0
                seat[i][4] = 0
                ans.append([i*5+1, i*5+2, i*5+3, i*5+4, i*5+5])
                flag = True
                break
        # 没有连续的座位了
        if not flag:
            t = []
            for i in range(20):
                for j in range(5):
                    if seat[i][j] == 1:
                        seat[i][j] = 0
                        t.append(i*5+j+1)
                        if len(t) == 5:
                            ans.append(t)
                            flag = True
                            break
                if flag:
                    break

for a in ans:
    for i in a:
        print(i, end=' ')
    print()