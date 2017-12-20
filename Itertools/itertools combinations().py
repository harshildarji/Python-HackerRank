# itertools.combinations()
# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

s = input().split()
for i in range(1, int(s[1])+1):
    for j in combinations(sorted(s[0].upper()), i):
        print(''.join(j))
