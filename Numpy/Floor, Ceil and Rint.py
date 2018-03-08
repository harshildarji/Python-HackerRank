# Floor, Ceil and Rint
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy
a = numpy.array(input().split(), float)
print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep = '\n')
