# Time Delta
# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime

def dateTime():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')

r = []
for _ in range(int(input().strip())):
    t1 = dateTime(); t2 = dateTime()
    r.append(int(abs(t1 - t2).total_seconds()))
print(*r, sep = '\n')
