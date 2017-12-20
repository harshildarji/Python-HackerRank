# itertools.product()
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*list(product(A, B)), sep = ' ')
