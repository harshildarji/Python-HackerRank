# Zeros and Ones
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy
t = tuple(map(int, input().split()))
print(numpy.zeros(t, dtype = numpy.int))
print(numpy.ones(t, dtype = numpy.int))
