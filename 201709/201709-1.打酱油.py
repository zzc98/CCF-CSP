n = int(input())
n = n//10
total = 0
num5 = n//5
total += num5 * 7
n = n - num5*5
num3 = n//3
total += num3*4
n = n - num3*3
total += n
print(total)
