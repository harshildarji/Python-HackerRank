# itertools.combinations_with_replacement()
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

line = input().split()
result = [''.join(j) for j in combinations_with_replacement(sorted(line[0].upper()), int(line[1]))]
print(*result, sep = '\n')
