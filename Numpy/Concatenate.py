# Concatenate
# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy
n, m, p = map(int, input().split())
a = numpy.array([input().split()[:p] for _ in range(n+m)], int)
print(a)
