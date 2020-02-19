n = int(input())
string = input().split()
num = []
for s in string:
    num.append(int(s))
num.sort()
max_num = num[0]
max_length = 1
temp_num = num[0]
temp_length = 1
for i in range(1, n):
    if num[i] == temp_num:
        temp_length += 1
    else:
        if temp_length > max_length:
            max_length = temp_length
            max_num = temp_num
        temp_num = num[i]
        temp_length = 1
if temp_length > max_length:
    print(temp_num)
else:
    print(max_num)
