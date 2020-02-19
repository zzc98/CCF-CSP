import sys

data = []
paragraph = False
list_flag = False
for line in sys.stdin:
    # 区块
    line = line.strip()
    if '#' in line:                          # 标题
        count = line.count("#")              # 计算是第几标题
        temp = line.split('#')[-1].strip()   # 这里分割最好不要用“空格”防止标题含有空格
        temp = "<h" + str(count) + ">" + temp + "</h" + str(count) + ">"
    elif '*' in line:                        # 无序列表
        if not list_flag:
            data.append('<ul>')
            list_flag = True
        temp = line.split("*")[-1].strip()   # 采用“*”分割
        temp = "<li>" + temp + "</li>"
    else:                                    # 段落
        if line and not paragraph:           # 首次出现段落
            temp = '<p>' + line
            paragraph = True
        elif line and paragraph:          # 中间出现段落
            temp = line
        elif line == '' and paragraph:    # 段落结束，修改data最后一个元素的值（即加上'</p>'）
            data[-1] = data[-1] + '</p>'
            paragraph = False
            temp = ''
        elif line == '' and list_flag:  # 无序列表结束
            data.append("</ul>")
            temp = ""
            list_flag = False
        else:
            temp = ''
            paragraph = False
            list_flag = False

    # 行内
    # 强调
    i = 1                                   # 标记是第一个"_"，还是第二个
    while '_' in temp:                      # 注意强调以及超链接都可能多个，所以用无限循环
        index_1 = temp.find('_')
        if i == 1:
            temp = temp[:index_1] + '<em>' + temp[index_1 + 1:]
            i = 2
        else:
            temp = temp[:index_1] + '</em>' + temp[index_1 + 1:]
            i = 1
    # 超链接
    while '[' in temp:                      # 注意这里是while，可能有多个超链接
        i1 = temp.find('[')
        i2 = temp.find(']', i1 + 1)
        i3 = temp.find('(', i2 + 1)
        i4 = temp.find(')', i3 + 1)
        temp = temp[:i1] + '<a href="' + \
            temp[(i3 + 1):i4] + '">' + temp[(i1 + 1):i2] + \
            "</a>" + temp[(i4 + 1):]

    data.append(temp)                       # 将转化后的html加入data
if paragraph:                            # 当以段落结束时
    data[-1] = data[-1] + '</p>'
if list_flag:                        # 当以无序列表结束时
    data.append("</ul>")
for d in data:
    if d == '':
        continue
    print(d)
