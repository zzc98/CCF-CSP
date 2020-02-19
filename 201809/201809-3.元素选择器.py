class Node:
    def __init__(self, label, nid='', children=[], parent=None, level=0, row=1):
        self.label = label
        self.nid = nid
        self.children = children
        self.parent = parent
        self.level = level
        self.row = row

    def match(self, string):
        if string[0] == '#':
            return self.nid == string
        return self.label == string.lower()


def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    root = Node(input().lower(), '', [], None, 0, 1)
    for i in range(1, n):
        s = input()
        l = s.count('.')//2
        p = root
        for j in range(1, l):
            p = p.children[-1]
        s = s.replace('.',  '')
        s = s.split()
        if len(s) == 1:
            t = Node(s[0].lower(), '', [], p, l, i+1)
            p.children.append(t)
        else:
            t = Node(s[0].lower(), s[1], [], p, l, i+1)
            p.children.append(t)
    ans = []
    for _ in range(m):
        s = input().split()
        match_len = len(s)
        an = []
        # 宽度优先遍历
        # 检测完最后一个，逐个向上检查父亲节点
        q = [root]
        while len(q) != 0:
            h = q.pop(0)
            p = h
            flag = True
            for i in range(match_len-1, -1, -1):
                try:
                    if not p.match(s[i]):
                        flag = False
                        break
                    p = p.parent
                except:
                    flag = False
                    break
            if flag:
                an.append(h.row)
            q.extend(h.children)
        ans.append(an)

    for an in ans:
        print(len(an), end=' ')
        for a in an:
            print(a, end=' ')
        print()


if __name__ == "__main__":
    main()

"""
11 5
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
........p #two
p
#subtitle
h3
div p
div div p

3 6 9 11
1 6
0 
2 9 11
1 11
"""
