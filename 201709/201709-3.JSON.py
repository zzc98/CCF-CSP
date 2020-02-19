string = input().split()
n, m = int(string[0]), int(string[1])
keys, dic = [], []
string = ''
for _ in range(n):
    string += input()
json=eval(string)
querys = list()
for _ in range(m):
    querys.append(input())
for query in querys:
    query = query.split('.')
    dic = json
    try:
        for q in query:
            dic = dic[q]
        if isinstance(dic, str):
            print('STRING '+ dic)
        else:
            print('OBJECT')
    except:
        print('NOTEXIST')
"""
10 5
{
"firstName": "John",
"lastName": "Smith",
"address": {
"streetAddress": "2ndStreet",
"city": "NewYork",
"state": "NY"
},
"esc\\aped": "\"hello\""
}
firstName
address
address.city
address.postal
esc\aped
-------
STRING John
OBJECT
STRING NewYork
NOTEXIST
STRING "hello"
"""

# string = input().split()
# n, m = int(string[0]), int(string[1])
# keys, dic = [], []
# for _ in range(n):
#     string = input()
#     if '{' != string[-1] and '}' != string[0]:
#         length = len(string)
#         temp = ''
#         i = 0
#         while i < length:
#             if string[i] != '\\':
#                 temp += string[i]
#                 i += 1
#             else:
#                 temp += string[i+1]
#                 i += 2
#         t = temp.split(':')
#         if ',' == t[1][-1]:
#             k, v = t[0][1:-1], t[1][2:-2]
#         else:
#             k, v = t[0][1:-1], t[1][2:-1]
#         dic[-1][k] = v
#     elif '{' == string[-1]:
#         keys.append(string[1:-4])
#         dic.append(dict())
#     elif len(string) == 2: 
#         k = keys.pop(-1)
#         v = dic.pop(-1)
#         dic[-1][k] = v
# json = dic[0]
# string = ''
# for _ in range(n):
#     string += input()

# json=eval(string)
# querys = list()
# for _ in range(m):
#     querys.append(input())
# for query in querys:
#     query = query.split('.')
#     dic = json
#     try:
#         for q in query:
#             dic = dic[q]
#         if isinstance(dic, str):
#             print('STRING '+ dic)
#         else:
#             print('OBJECT')
#     except:
#         print('NOTEXIST')