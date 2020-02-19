import time
MONTH_DIC = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
WEEK_DIC = {'Sun': 0, 'Mon': 1, 'Tue': 2,
            'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}


class Task:
    def __init__(self, string):
        string = string.split()
        self.name = string[-1]
        # 分钟：0-59
        s = string[0]
        if s == '*':
            self.minute = '*'
        else:
            s = s.split(',')
            self.minute = []
            for q in s:
                if '-' in q:
                    q = q.split('-')
                    start, end = int(q[0]), int(q[1])
                    for i in range(start, end+1):
                        self.minute.append(i)
                else:
                    self.minute.append(int(q))
        # 小时：0-23
        s = string[1]
        if s == '*':
            self.hour = '*'
        else:
            s = s.split(',')
            self.hour = []
            for q in s:
                if '-' in q:
                    q = q.split('-')
                    start, end = int(q[0]), int(q[1])
                    for i in range(start, end+1):
                        self.hour.append(i)
                else:
                    self.hour.append(int(q))
        # 日期：1-31
        s = string[2]
        if s == '*':
            self.day = '*'
        else:
            s = s.split(',')
            self.day = []
            for q in s:
                if '-' in q:
                    q = q.split('-')
                    start, end = int(q[0]), int(q[1])
                    for i in range(start, end+1):
                        self.day.append(i)
                else:
                    self.day.append(int(q))
        # 月份 1-12 / Jan - Dec
        s = string[3]
        if s == '*':
            self.month = '*'
        else:
            s = s.split(',')
            self.month = []
            for q in s:
                if '-' in q:
                    q = q.split('-')
                    try:
                        start, end = int(q[0]), int(q[1])
                    except:
                        start, end = MONTH_DIC[q[0]], MONTH_DIC[q[1]]
                    for i in range(start, end+1):
                        self.month.append(i)
                else:
                    try:
                        self.month.append(int(q))
                    except:
                        self.month.append(MONTH_DIC[q])
        # 星期  0-6 / Sun - Sat
        s = string[4]
        if s == '*':
            self.week = '*'
        else:
            s = s.split(',')
            self.week = []
            for q in s:
                if '-' in q:
                    q = q.split('-')
                    try:
                        start, end = int(q[0]), int(q[1])
                    except:
                        start, end = WEEK_DIC[q[0]], WEEK_DIC[q[1]]
                    for i in range(start, end+1):
                        self.week.append(i)
                else:
                    try:
                        self.week.append(int(q))
                    except:
                        self.week.append(WEEK_DIC[q])

        self.check = [self.minute, self.hour, self.day, self.month, self.week]

    def match(self, mi, ho, md, mo, wd):
        temp = [mi, ho, md, mo, wd]
        flag = True
        for i in range(5):
            if self.check[i] == '*':
                continue
            if temp[i] not in self.check[i]:
                flag = False
                break
        if flag:
            return (True, self.name)
        else:
            return (False, '')

    def show(self):
        for i in range(5):
            print(self.check[i], end=' ')
        print()

if __name__ == "__main__":
    string = input().split()
    n, startTime, endTime = int(string[0]), string[1], string[2]
    startTime = int(time.mktime(time.strptime(startTime, "%Y%m%d%H%M")))
    endTime = int(time.mktime(time.strptime(endTime, "%Y%m%d%H%M")))
    rules = []
    for _ in range(n):
        s = input()
        rules.append(Task(s))
    for t in rules:
        t.show()
    ans = []
    for i in range(startTime, endTime, 60):
        ts = time.localtime(i)
        standTime = time.strftime("%Y%m%d%H%M", ts)
        minute = ts.tm_min
        hour = ts.tm_hour
        mday = ts.tm_mday
        mon = ts.tm_mon
        wday = (ts.tm_wday+8) % 7
        for t in rules:
            res = t.match(minute, hour, mday, mon, wday)
            if res[0]:
                ans.append(standTime + ' '+res[1])

    for a in ans:
        print(a)


"""
3 201711170032 201711222352
0 7 * * 1,3-5 get_up
30 23 * * Sat,Sun go_to_bed
15 12,18 * * * have_dinner

----
201711170700 get_up
201711171215 have_dinner
201711171815 have_dinner
201711181215 have_dinner
201711181815 have_dinner
201711182330 go_to_bed
201711191215 have_dinner
201711191815 have_dinner
201711192330 go_to_bed
201711200700 get_up
201711201215 have_dinner
201711201815 have_dinner
201711211215 have_dinner
201711211815 have_dinner
201711220700 get_up
201711221215 have_dinner
201711221815 have_dinner
"""
