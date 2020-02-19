s = input().split()
row, col = int(s[0]), int(s[1])
pic = []
for _ in range(row):
    s = input().split()
    t = [i for i in s]
    pic.append(t)

for j in range(col-1,-1,-1):
    for i in range(row):
        print(pic[i][j], end=' ')
    print()