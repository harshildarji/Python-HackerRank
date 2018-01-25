# Athlete Sort
# https://www.hackerrank.com/challenges/python-sort-sort/problem

n, m = map(int, input().split())
details = []
for _ in range(n):
    details.append(list(map(int, input().split()))[:m])
k = int(input().strip())
for i in sorted(details, key = lambda x: x[k]): print(*i, sep = ' ')
