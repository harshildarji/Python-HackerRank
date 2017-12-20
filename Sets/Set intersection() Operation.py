# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input().strip())
n1 = set([int(i) for i in input().split()][:n])
b = int(input().strip())
b1 = set([int(i) for i in input().split()][:b])
print(len(n1.intersection(b1)))
