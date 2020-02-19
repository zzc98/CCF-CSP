"""
没有考虑到考点9和考点10，只得了80分
"""

def sample(string, coef):
    # 没有括号的单元处理
    length = len(string)
    if length == 0:
        return {}
    i = 0
    e_dict = {}
    while i < length:
        if 'A' <= string[i] <= 'Z':
            if i+1 < length and 'a' <= string[i+1] <= 'z':
                ele = string[i] + string[i+1]
                start = i+2
            else:
                ele = string[i]
                start = i+1
            num = 0
            while start < length:
                if '0' <= string[start] <= '9':
                    num = num*10 + int(string[start])
                    start += 1
                else:
                    break
            if num == 0:
                num = 1
            e_dict[ele] = e_dict.get(ele, 0) + num
            i = start
    for i in e_dict:
        e_dict[i] = e_dict[i] * coef
    return e_dict


def main():
    n = int(input())
    ans = []
    for _ in range(n):
        equation = input()
        left, right = equation.split('=')
        left_items = left.split('+')
        right_items = right.split('+')
        # 左边项
        e_dict_list = []
        for item in left_items:
            length = len(item)
            i = 0
            # 系数
            coef = 0
            while i < length:
                if '0' <= item[i] <= '9':
                    coef = coef * 10 + int(item[i])
                    i += 1
                else:
                    break
            if coef == 0:
                coef = 1
            # 寻找基本单元
            new_item = '(' + item[i:] + ')'
            length = len(new_item)
            i = 0
            chars = []  # 栈
            while i < length:
                key = new_item[i]
                if key != ')':
                    chars.append(key)
                    i += 1
                else:
                    # 基本单元
                    temp = ''
                    c = chars.pop(-1)
                    while c != '(':
                        temp = c + temp
                        c = chars.pop(-1)
                    # 后置系数
                    num = 0
                    i = i + 1
                    while i < length:
                        if '0' <= new_item[i] <= '9':
                            num = num*10 + int(new_item[i])
                            i += 1
                        else:
                            break
                    if num == 0:
                        num = 1
                    e_dict_list.append(sample(temp, num*coef))
        # 字典整理
        final_dict = {}
        for dic in e_dict_list:
            for key in dic:
                final_dict[key] = final_dict.get(key, 0) + dic[key]


        # 右边项
        e_dict_list = []
        for item in right_items:
            length = len(item)
            i = 0
            # 系数
            coef = 0
            while i < length:
                if '0' <= item[i] <= '9':
                    coef = coef * 10 + int(item[i])
                    i += 1
                else:
                    break
            if coef == 0:
                coef = 1
            # 寻找基本单元
            new_item = '(' + item[i:] + ')'
            length = len(new_item)
            i = 0
            chars = []  # 栈
            while i < length:
                key = new_item[i]
                if key != ')':
                    chars.append(key)
                    i += 1
                else:
                    # 基本单元
                    temp = ''
                    c = chars.pop(-1)
                    while c != '(':
                        temp = c + temp
                        c = chars.pop(-1)
                    # 后置系数
                    num = 0
                    i = i + 1
                    while i < length:
                        if '0' <= new_item[i] <= '9':
                            num = num*10 + int(new_item[i])
                            i += 1
                        else:
                            break
                    if num == 0:
                        num = 1
                    e_dict_list.append(sample(temp, num*coef))

        flag = True


        # 字典整理
        try:
            for dic in e_dict_list:
                for key in dic:
                    final_dict[key] = final_dict[key] - dic[key]
        except:
            flag = False

        for key in final_dict:
            if final_dict[key] != 0:
                flag = False
                break
        if flag:
            ans.append('Y')
        else:
            ans.append('N')

    for i in ans:
        print(i)


if __name__ == "__main__":
    main()


"""
H2+O2=H2O
2H2+O2=2H20
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
3Ba(OH)2+2H3PO4=6H2O+Ba3(PO4)2
3Ba(OH)2+2H3PO4=Ba3(PO4)2+6H2O
4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O
Cu+As=Cs+Au
"""
# 4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH
