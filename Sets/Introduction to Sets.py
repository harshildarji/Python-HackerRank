# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

n = int(input().strip())
values = set([int(i) for i in input().split()][:n])
print("%.3f" % (sum(values)/len(values)))
