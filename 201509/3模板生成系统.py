s = input().split()
n, m = int(s[0]), int(s[1])
html = []
for _ in range(n):
    s = input()
    html.append(s)
dic = {}
for _ in range(m):
    s = input().split()
    v = ' '.join(s[1:])
    dic[' '+s[0]+' '] = v[1:-1]


def parse(string):
    length = len(string)
    ans = ''
    i = 0
    var = False
    name = ''
    while i < length:
        if string[i] == '{' and i+1 < length and string[i+1] == '{':
            var = True
            i = i + 2
            continue
        elif string[i] == '}' and i+1 < length and string[i+1] == '}':
            if var:
                ans = ans + dic.get(name, '')
            else:
                ans = ans + '}}'
            name = ''
            var = False
            i = i+2
        else:
            if var:
                name = name + string[i]
            else:
                ans = ans + string[i]
            i += 1
    if var:
        ans = ans + name
    return ans


for s in html:
    print(parse(s))
