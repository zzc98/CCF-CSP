game = []
for _ in range(15):
    string = input().split()
    game.append(string)
game.append(['1']*10)
game.append(['1']*10)
game.append(['1']*10)
game.append(['1']*10)

kuai = []
for _ in range(4):
    string = input().split()
    kuai.append(string)
row, col = 0, int(input())-1
flag = True
while flag:
    for i in range(4):
        for j in range(4):
            if kuai[i][j] == '1' and game[i+row][j+col] == '1':
                flag = False
                break
        if not flag:
            break
    if flag:
        row += 1
row -= 1
for i in range(4):
    for j in range(4):
        if kuai[i][j] == '1':
            game[i+row][j+col] = '1'

for i in range(15):
    for j in range(10):
        print(game[i][j], end=' ')
    print()