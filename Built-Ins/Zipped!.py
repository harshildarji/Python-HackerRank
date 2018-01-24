# Zipped!
# https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int, input().split())
marks = []
for _ in range(x):
    marks.append(list(map(float, input().split()))[:n])
for i in zip(*marks): print(sum(i) / x)
