n = int(input())
s = input().split()
nums = [int(t) for t in s]
dic = {}
for i in nums:
    dic[i] = dic.get(i, 0) + 1
p = []
for k in dic:
    p.append((dic[k]*(-1), k))
p.sort()
for item in p:
    print(item[1], item[0]*(-1))

"""
12
5 2 3 3 1 3 4 2 5 2 3 5

"""
