# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input().strip())
n1 = set([int(i) for i in input().split()][:n])
m = int(input().strip())
m1 = set([int(i) for i in input().split()][:m])
for i in sorted(n1.difference(m1).union(m1.difference(n1))):
    print(i)
