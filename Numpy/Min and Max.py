# Min and Max
# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy
n, m = map(int, input().split())
a = numpy.array([input().split()[:m] for _ in range(n)], int)
print(numpy.max(numpy.min(a, axis = 1)))
