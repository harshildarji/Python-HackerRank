# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input().strip())
n1 = set([int(i) for i in input().split()][:n])
b = int(input().strip())
b1 = set([int(i) for i in input().split()][:b])
print(len(n1.union(b1)))
