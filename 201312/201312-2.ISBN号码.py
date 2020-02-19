string = input()
isbn = string.replace('-', '')
ans = 0
for i in range(9):
    ans += int(isbn[i]) * (i+1)
ans = ans % 11
if ans == 10:
    if string[-1] == 'X':
        print('Right')
    else:
        print(string[:-1] + 'X')
else:
    try:
        if ans == int(isbn[-1]):
            print('Right')
        else:
            print(string[:-1] + str(ans))
    except:
        print(string[:-1] + str(ans))
