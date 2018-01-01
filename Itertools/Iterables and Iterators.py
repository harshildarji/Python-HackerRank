# Iterables and Iterators
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

n = int(input().strip())
line = [i for i in input().split()][:n]
k = int(input().strip())
count = 0
comb = list(combinations(line, k))
for i in comb:
    if 'a' in i: count += 1
print(count / len(comb))
