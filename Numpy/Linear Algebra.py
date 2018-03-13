# Linear Algebra
# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy
n = int(input().strip())
a = numpy.array([input().split()[:n] for _ in range(n)], float)
print(numpy.linalg.det(a))
