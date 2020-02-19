import sys


class My:
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell


prices = set()
remove = []
record = [('cancel')]

for line in sys.stdin:
    if line == '\n':
        break
    line = line.split()
    if line[0] != 'cancel':
        p, s = float(line[1]), int(line[2])
        record.append((line[0], p, s))
        prices.add(p)
    else:
        record.append(('cancel'))
        remove.append(int(line[1]))

remove.sort()
remove.reverse()
for i in remove:
    record.pop(i)

dic = {}
for price in prices:
    buy, sell = 0, 0
    for r in record:
        if r[0] == 'buy' and r[1] >= price:
            buy += r[2]
        elif r[0] == 'sell' and r[1] <= price:
            sell += r[2]
    t = My(buy, sell)
    dic[price] = t

ans_price, ans_total = 0, 0
for price in dic:
    t = min(dic[price].sell, dic[price].buy)
    if ans_total <= t:
        ans_price = price
        ans_total = t

print("{:.2f} {}".format(ans_price, ans_total))

"""
buy 9.25 100
buy 8.88 175
sell 9.00 1000
buy 9.00 400
sell 8.92 400
cancel 1
buy 100.00 50
"""
