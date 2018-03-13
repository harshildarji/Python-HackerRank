# Dot and Cross
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy
n = int(input().strip())
a, b = (numpy.array([input().split() for _ in range(n)], int) for _ in range(2))
print(numpy.dot(a, b))
