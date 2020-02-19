n = int(input())
prefList = []


def standardIP(s):
    temp1 = s.split('/')
    if len(temp1) == 1:
        temp2 = temp1[0].split('.')
        l = len(temp2)
        if l == 1:
            return temp1[0] + '.0.0.0/' + str(8)
        elif l == 2:
            return temp1[0] + '.0.0/' + str(16)
        elif l == 3:
            return temp1[0] + '.0/' + str(24)
        else:
            return temp1[0] + '/' + str(32)
    else:
        temp2 = temp1[0].split('.')
        l = len(temp2)
        if l == 1:
            return temp1[0] + '.0.0.0/' + temp1[1]
        elif l == 2:
            return temp1[0] + '.0.0/' + temp1[1]
        elif l == 3:
            return temp1[0] + '.0/' + temp1[1]
        else:
            return temp1[0] + '/' + temp1[1]


def repretation(s):
    s = s.split('/')
    ss = s[0].split('.')
    return (int(ss[0]), int(ss[1]), int(ss[2]), int(ss[3]), int(s[1]))


def show(s):
    return str(s[0])+ '.' + str(s[1]) + '.' + str(s[2]) + '.' + str(s[3]) + '.' + str(s[4])


for _ in range(n):
    s = standardIP(input())
    s = repretation(s)
    prefList.append(s)

prefList.sort()

for pref in prefList:
    print(show(pref))


"""
2
1
2

1.0.0.0/8
2.0.0.0/8
-------------------
2
10/9
10.128/9

10.0.0.0/8
-------------------
2
0/1
128/1

0.0.0.0/0
"""
