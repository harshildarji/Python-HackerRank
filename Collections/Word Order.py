# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    line = input()
    d[line] = d.setdefault(line, 0) + 1
print(len(d))
for key in d:
    print(d[key], end=' ')
