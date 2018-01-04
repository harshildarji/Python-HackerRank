# Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input().strip())
d = OrderedDict()
for _ in range(n):
    line = input().split()
    if ' '.join(line[:-1]) not in d: d[' '.join(line[:-1])] = int(line[-1])
    else: d[' '.join(line[:-1])] += int(line[-1])
for i in d: print(i, d[i])
