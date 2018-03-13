# Inner and Outer
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy
a, b = (numpy.array(input().split(), int) for _ in range(2))
print(numpy.inner(a, b), numpy.outer(a, b), sep = '\n')
