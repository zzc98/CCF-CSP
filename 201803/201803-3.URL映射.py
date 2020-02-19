class Rule:
    def __init__(self, string):
        string = string.split()
        self.name = string[1]
        string = string[0]
        self.pattern = string.split('/')
        self.length = len(self.pattern)

    def match(self, string):
        rn = []
        string = string.split('/')
        slen = len(string)
        i, j = 0, 0
        flag = True
        while i < self.length and j < slen:
            if self.pattern[i] == '<int>':
                try:
                    rn.append(int(string[j]))
                except:
                    flag = False
                    break
            elif self.pattern[i] == '<str>':
                rn.append(string[j])
            elif self.pattern[i] == '<path>':
                t = string[j]
                for k in range(j+1, slen):
                    t = t + '/' + string[k]
                rn.append(t)
                j = slen-1
            else:
                if string[j] != self.pattern[i]:
                    flag = False
                    break
            i += 1
            j += 1
        if flag and i == self.length and j == slen:
            temp = self.name
            for r in rn:
                temp = temp + ' ' + str(r)
            return [True, temp]
        else:
            return [False, '']


def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    rules = []
    for _ in range(n):
        rules.append(Rule(input()))
    ans = []
    for _ in range(m):
        string = input()
        flag = False
        for r in rules:
            data = r.match(string)
            if data[0]:
                ans.append(data[1])
                flag = True
                break
        if not flag:
            ans.append('404')

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()

"""
5 4
/articles/2003/ special_case_2003
/articles/<int>/ year_archive
/articles/<int>/<int>/ month_archive
/articles/<int>/<int>/<str>/ article_detail
/static/<path> static_serve
/articles/2004/
/articles/1985/09/aloha/
/articles/hello/
/static/js/jquery.js
--------------------------------------------
year_archive 2004
article_detail 1985 9 aloha
404
static_serve js/jquery.js
"""
