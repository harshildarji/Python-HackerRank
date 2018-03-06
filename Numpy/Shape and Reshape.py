# Shape and Reshape
# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy
a = numpy.array(list(map(int, input().split())))
print(numpy.reshape(a, (3, 3)))
