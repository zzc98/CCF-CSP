n = int(input())
students = [i for i in range(1, n+1)]
k = int(input())
for _ in range(k):
    s = input().split()
    p, q = int(s[0]), int(s[1])
    index = students.index(p)
    students.remove(p)
    try:
        students.insert(index+q, p)
    except:
        students.append(p)
for student in students:
    print(student, end=' ')

"""
8
3
3 2
8 -3
3 -2
-------------
1 2 4 3 5 8 6 7
"""