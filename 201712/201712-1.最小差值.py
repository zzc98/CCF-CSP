n = int(input())
string = input().split()
data = [int(s) for s in string]
data.sort()
min_value = float('INF')
for i in range(1, n):
    d = data[i] - data[i-1]
    if d < min_value:
        min_value = d

print(min_value)