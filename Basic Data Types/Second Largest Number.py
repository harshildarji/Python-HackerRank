# Find the Second Largest Number
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input().strip())
a = set([int(i) for i in input().split()][:n])
print(sorted(a)[-2])
