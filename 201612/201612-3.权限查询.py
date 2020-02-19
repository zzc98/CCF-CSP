class Privilege:
    def __init__(self, name, slevel=-1):
        self.name = name
        self.level = slevel


# 记录权限
p_num = int(input())
Pdict = {}  # 权限名 -> 等级 （默认-1）
for _ in range(p_num):
    string = input()
    if ':' in string:
        string = string.split(':')
        Pdict[string[0]] = int(string[1])
    else:
        Pdict[string] = -1

# 记录角色
r_num = int(input())
Rdict = {}  # 角色名 -> 权限列表（权限对象）
for _ in range(r_num):
    string = input().split()
    r_name = string[0]
    r_list = list()
    for i in range(int(string[1])):
        pri = string[i+2]
        if ':' in pri:
            pri = pri.split(':')
            P = Privilege(pri[0], int(pri[1]))
        else:
            P = Privilege(pri)
        r_list.append(P)
    Rdict[r_name] = r_list

# 记录用户
u_num = int(input())
Udict = {}  # 用户名 -> 角色名列表
for _ in range(u_num):
    string = input().split()
    u_name = string[0]
    u_list = list()
    for i in range(int(string[1])):
        u_list.append(string[i+2])
    Udict[u_name] = u_list


# 记录查询
q_num = int(input())
q_list = []
for _ in range(q_num):
    q_list.append(input())


# 解题
def parse(string):
    string = string.split()
    u, task = string[0], string[1]
    if ':' in task:
        task = task.split(':')
        t_name = task[0]
        t_level = int(task[1])
    else:
        t_name = task
        t_level = -1
    if t_name not in Pdict or u not in Udict:
        return 'false'

    max_level = -1
    roles = Udict[u]  # 拥有的角色名字
    for r in roles:
        ps = Rdict[r]  # 角色拥有的权限对象列表
        for p in ps:  # 每一个权限
            if p.name == t_name:
                if Pdict[t_name] == -1:  # 说明这是不分等级的权限，返回true or false
                    return 'true'
                else:
                    max_level = max(max_level, p.level)
    if Pdict[t_name] == -1:  # 不分等级的权限，返回true or false
        return 'false'
    else:  # 分等级的权限
        if t_level == -1:  # 不带等级查询
            if max_level == -1:
                return 'false'
            else:
                return max_level
        else:  # 带等级的查询
            return 'true' if max_level >= t_level else 'false'


ans = []
for q in q_list:
    a = parse(q)
    ans.append(a)
for a in ans:
    print(a)

"""
3
crm:2
git:3
game
4
hr 1 crm:2
it 3 crm:1 git:1 game
dev 2 git:3 game
qa 1 git:2
3
alice 1 hr
bob 2 it qa
charlie 1 dev
9
alice game
alice crm:2
alice git:0
bob git
bob poweroff
charlie game
charlie crm
charlie git:3
malice game


false
true
false
2
false
true # charlie game
false
true
false


"""
