# itertools.combinations()
# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

s, k = input().split()
words = []
for i in range(1, int(k)+1):
    words.append([''.join(sorted(i)) for i in list(combinations(s.upper(), i))])
for i in words:
    print(*sorted(i), sep = '\n')
