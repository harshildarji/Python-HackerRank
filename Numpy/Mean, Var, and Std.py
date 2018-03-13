# Mean, Var, and Std
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy
n, m = map(int, input().split())
a = numpy.array([input().split()[:m] for _ in range(n)], int)
print(numpy.mean(a, axis = 1), numpy.var(a, axis = 0), numpy.std(a), sep = '\n')
