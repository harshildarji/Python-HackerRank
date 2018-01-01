# Maximize It!
# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

k, m = map(int, input().split())
l = []
for i in range(k):
    l.append(pow(x, 2) for x in list(map(int, input().split()))[1:])
ps = map(sum, itertools.product(*l))
mps = max(map(lambda p: p % m, ps))
print(mps)
