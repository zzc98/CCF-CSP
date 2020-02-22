"""
只得了80分
"""
def sample(t_dict, string, coef): 
    """
    params string:基本单元解析，不含括号
    params coef:后置系数
    """
    length = len(string)
    i = 0
    e_dict = {} # 基本单元字典
    while i < length:
        if 'A' <= string[i] <= 'Z':  # 基本元素
            ni = i+1
            if ni < length and 'a' <= string[ni] <= 'z':
                ele = string[i] + string[ni]
                start = i + 2
            else:
                ele = string[i]
                start = i+1
            num = ''
            while start < length:  # 后置系数
                if '0' <= string[start] <= '9':
                    num = num + string[start]
                    start += 1
                else:
                    break
            num = 1 if num == '' else int(num)
            e_dict[ele] = e_dict.get(ele, 0) + num
            i = start
    for t in e_dict:
        t_dict[t] = t_dict.get(t, 0) + e_dict[t] * coef


def parse(equation):
    equation = equation.split('=')
    left, right = equation[0], equation[1]
    left_items = left.split('+')
    right_items = right.split('+')
    # 左边项
    left_dict = {}  # 左侧总字典
    for item in left_items:
        length = len(item)
        i = 0  # 游标
        # 前置系数
        coef = ''
        while i < length:
            if '0' <= item[i] <= '9':
                coef = coef + item[i]
                i += 1
            else:
                break
        coef = 1 if coef == '' else int(coef)
        # 解析单元
        item_dic = [{}]  # 字典栈
        chars = []  # 字符栈
        new_item = '(' + item[i:] + ')'
        length = len(new_item)
        i = 0
        while i < length:
            key = new_item[i]
            if key != ')':
                chars.append(key)
                if key == '(':
                    item_dic.append({})
                i += 1
            else:
                # 基本单元
                temp = ''
                c = chars.pop(-1)
                while c != '(':
                    temp = c + temp
                    c = chars.pop(-1)
                # 后置系数
                num = ''
                i = i + 1
                while i < length:
                    if '0' <= new_item[i] <= '9':
                        num = num + new_item[i]
                        i += 1
                    else:
                        break
                num = 1 if num == '' else int(num)
                sample(item_dic[-1], temp, num)
                temp_dict = item_dic.pop(-1)
                for t in temp_dict:
                    item_dic[-1][t] = item_dic[-1].get(t, 0) + temp_dict[t]
        
        for t in item_dic[0]:
            left_dict[t] = left_dict.get(t, 0) + item_dic[0][t] * coef  # 左侧总字典

    # 右边项
    right_dict = {}
    for item in right_items:
        length = len(item)
        i = 0  # 游标
        # 前置系数
        coef = ''
        while i < length:
            if '0' <= item[i] <= '9':
                coef = coef + item[i]
                i += 1
            else:
                break
        coef = 1 if coef == '' else int(coef)
        # 解析单元
        item_dic = [{}]  # 字典栈
        chars = []  # 字符栈
        new_item = '(' + item[i:] + ')'
        length = len(new_item)
        i = 0
        while i < length:
            key = new_item[i]
            if key != ')':
                chars.append(key)
                if key == '(':
                    item_dic.append(dict())
                i += 1
            else:
                # 基本单元
                temp = ''
                c = chars.pop(-1)
                while c != '(':
                    temp = c + temp
                    c = chars.pop(-1)
                # 后置系数
                num = ''
                i = i + 1
                while i < length:
                    if '0' <= new_item[i] <= '9':
                        num = num + new_item[i]
                        i += 1
                    else:
                        break
                num = 1 if num == '' else int(num)
                sample(item_dic[-1], temp, num)
                temp_dict = item_dic.pop(-1)
                for t in temp_dict:
                    item_dic[-1][t] = item_dic[-1].get(t, 0) + temp_dict[t]
        for t in item_dic[0]:
            right_dict[t] = right_dict.get(t, 0) + item_dic[0][t] * coef
    
    return left_dict == right_dict
    


def main():
    n = int(input())
    ans = []
    for _ in range(n):
        flag = parse(input())
        if flag:
            ans.append('Y')
        else:
            ans.append('N')
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()


"""
11
H2+O2=H2O
2H2+O2=2H2O
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
3Ba(OH)2+2H3PO4=6H2O+Ba3(PO4)2
3Ba(OH)2+2H3PO4=Ba3(PO4)2+6H2O
4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O
4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH
Cu+As=Cs+Au
"""

