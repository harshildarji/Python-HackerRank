# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input().strip())
t = tuple([int(i) for i in input().split()][0:n])

print(hash(t))
