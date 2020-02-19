class Window:
    def __init__(self, x1, y1, x2, y2, name):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name

    def have(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2


s = input().split()
n, m = int(s[0]), int(s[1])
windows = []
for i in range(1, n+1):
    s = input().split()
    x1, y1, x2, y2 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    w = Window(x1, y1, x2, y2, i)
    windows.append(w)
ans = []
for _ in range(m):
    s = input().split()
    xx, yy = int(s[0]), int(s[1])
    i = n-1
    while i >= 0:
        if windows[i].have(xx, yy):
            break
        i -= 1
    if i >= 0:
        w = windows.pop(i)
        ans.append(w.name)
        windows.append(w)
    else:
        ans.append('IGNORED')
for a in ans:
    print(a)
