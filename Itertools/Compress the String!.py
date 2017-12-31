# Compress the String!
# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

data = input()
groups = []
for key, value in groupby(data):
    groups.append((len(list(value)), int(key)))
print(*groups)
