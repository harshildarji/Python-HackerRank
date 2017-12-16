# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
N = [int(i) for i in input().split()][:n]
A = set([int(i) for i in input().split()][:m])
B = set([int(i) for i in input().split()][:m])
print(sum((i in A) - (i in B) for i in N))
