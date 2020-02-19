def main():
    string = input()
    length = len(string)
    have, nohave = set(), set()
    i = 0
    while i < length:
        j = i+1
        if j < length:
            if string[j] == ':':
                have.add('-' + string[i])
                i += 2
            else:
                nohave.add('-' + string[i])
                i += 1
        else:
            nohave.add('-' + string[i])
            i += 1
    n = int(input())
    ans = []
    for _ in range(n):
        s = input().split()
        length = len(s)
        t = []
        i = 1
        while i < length:
            if s[i] in nohave:  # 无参选项
                if s[i] not in t:
                    t.append(s[i])
                i += 1
                continue
            else:
                if s[i] in have:  # 带参选项
                    if s[i] not in t:  # 第一次出现
                        j = i+1
                        if j < length:  # 有参数
                            t.append(s[i])
                            t.append(s[j])
                            i += 2
                            continue
                        else:  # 出错终止
                            break
                    else:  # 更新参数
                        j = i+1
                        if j < length:
                            new_value = s[j]
                            index = t.index(s[i])+1
                            t[index] = new_value
                            i += 2
                        else:
                            break
                else:
                    break
        length = len(t)
        temp = []
        i = 0
        while i < length:
            if t[i] in nohave:
                temp.append((t[i], ''))
                i += 1
            else:
                temp.append((t[i], t[i+1]))
                i += 2
        temp.sort()
        ans.append(temp)

    for i in range(n):
        a = ans[i]
        if len(a) == 0:  # 没有参数
            print('Case {}:'.format(i+1))
            continue
        else:
            print('Case {}:'.format(i+1), end='')
            for j in a:
                if j[0] in nohave:
                    print(' {}'.format(j[0]), end='')
                else:
                    print(' {} {}'.format(j[0], j[1]), end='')
            print()


if __name__ == "__main__":
    main()

"""
albw:x
4
ls -a -l -a documents -b
ls
ls -w 10 -x -w 15
ls -a -b -c -d -e -l

Case 1: -a -l
Case 2:
Case 3: -w 15 -x
Case 4: -a -b
"""
