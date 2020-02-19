n=int(input())
nums=input().split()
dic={}
for i in nums:
    dic[i] = dic.get(i, 0) + 1
    print(dic[i], end=' ')