# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input().strip())
result = True
for i in range(n):
    s = set(map(int, input().split()))
    if not s < A:
        result = False
print(result)
