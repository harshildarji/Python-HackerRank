# itertools.permutations()
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

line = input().split()
words = [''.join(i) for i in list(permutations(line[0].upper(), int(line[1])))]
print(*sorted(words), sep = '\n')

