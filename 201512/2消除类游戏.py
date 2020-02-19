s = input().split()
row, col = int(s[0]), int(s[1])
game = []
for i in range(row):
    s = input().split()
    t = []
    for j in range(col):
        t.append([s[j], False])
    game.append(t)

for i in range(row):
    for j in range(col-2):
        t = game[i][j][0]
        if game[i][j+1][0] == t and game[i][j+2][0] == t:
            game[i][j][1] = True
            game[i][j+1][1] = True
            game[i][j+2][1] = True

for j in range(col):
    for i in range(row-2):
        t = game[i][j][0]
        if game[i+1][j][0] == t and game[i+2][j][0] == t:
            game[i][j][1] = True
            game[i+1][j][1] = True
            game[i+2][j][1] = True

for i in range(row):
    for j in range(col):
        if game[i][j][1]:
            print('0', end=' ')
        else:
            print(game[i][j][0], end=' ')
    print()

"""
4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3

2 2 3 0 2
3 0 0 0 0
2 3 2 0 3
2 2 0 0 0
"""