# collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input().strip())
sizes = Counter(list(map(int, input().split()))[:n])
c = int(input().strip())
money = 0
for _ in range(c):
    s, m = map(int, input().split())
    if sizes[s] > 0: money += m; sizes[s] -= 1
print(money)
