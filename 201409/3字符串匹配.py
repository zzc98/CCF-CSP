target = input()
turn = int(input())
n = int(input())
ans = []
if turn == 1:  # 敏感
    for _ in range(n):
        s = input()
        if target in s:
            ans.append(s)
else: # 不敏感
    target = target.lower()
    for _ in range(n):
        s = input()
        s2 = s.lower()
        if target in s2:
            ans.append(s)
for a in ans:
    print(a)
