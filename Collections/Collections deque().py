# Collections.deque()
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

n = int(input().strip())
d = deque()
for _ in range(n):
    line = input().split()
    if len(line) > 1: exec('d.' + line[0] + "('" + line[1] + "')")
    else: exec('d.' + line[0] + '()')
print(*d)
