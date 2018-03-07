# Array Mathematics
# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy
n, m = map(int, input().split())
a, b = (numpy.array([input().split() for _ in range(n)], dtype = int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep = '\n')
