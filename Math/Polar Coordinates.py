# Polar Coordinates
# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import *

n = eval(input().strip())
print('%f\n%f' % (abs(n), phase(n)))
