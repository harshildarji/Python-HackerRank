# itertools.permutations()
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

line = input().split()
for i in permutations(sorted(line[0].upper()), int(line[1])):
    print(''.join(i))

