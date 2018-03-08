# Sum and Prod
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy
n, m = map(int, input().split())
a = numpy.array([input().split()[:m] for _ in range(n)], int)
print(numpy.prod(numpy.sum(a, axis = 0)))
