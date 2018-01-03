# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    s = input().strip()
    d[s].append(i+1)
for _ in range(m):
    s = input().strip()
    if s in d: print(' '.join(map(str, d[s])))
    else: print('-1')

