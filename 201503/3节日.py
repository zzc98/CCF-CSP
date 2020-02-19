s = input().split()
target = (int(s[0]), int(s[1]), int(s[2]))  # {0}月的第{1}个星期{2}
now_year, stop_year = int(s[3]), int(s[4])
offset = 0
for y in range(1850, now_year):
    offset += 2 if y % 400 == 0 or(y % 4 == 0 and y % 100 != 0) else 1
    offset = offset % 7
for y in range(now_year, stop_year+1):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for m in range(1, 13):  # 1 ~ 12
        if m == target[0]:  # 搜索到目标月
            sun = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 0: 0}  # 各出现了几次，0代表7
            flag = False
            now = (2 + offset) % 7  # 这个月1号是周几
            for i in range(1, dic[m] + 1):  # 计算天
                sun[now] = sun[now] + 1
                if ((now == 0 and target[2] == 7) or (now == target[2])) and sun[now] == target[1]:
                    print(str(y) + '/', end='')
                    if m < 10:
                        print('0' + str(m) + '/', end='')
                    else:
                        print(str(m) + '/', end='')
                    if i < 10:
                        print('0' + str(i))
                    else:
                        print(str(i))
                    flag = True
                    break
                now += 1
                now %= 7
            if not flag:
                print('none')

        offset += dic[m]
        offset = offset % 7
