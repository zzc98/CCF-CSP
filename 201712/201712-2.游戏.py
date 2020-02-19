string = input().split()
n, k = int(string[0]), int(string[1])
person = [i for i in range(1, n+1)]

now = 1
index = 0
remain = n
while remain > 1:
    if now % k == 0 or now % 10 == k:  # 淘汰该人
        person.pop(index)
        remain -= 1
        index = index % remain
    else: # 无人淘汰
        index = (index+1) % remain
    now += 1

print(person[0])
