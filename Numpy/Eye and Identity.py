# Eye and Identity
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy
n, m = map(int, input().split())
print(numpy.eye(n, m, k = 0))
