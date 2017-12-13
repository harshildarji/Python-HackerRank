# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

n = int(input().strip())
record = []

for i in range(0, n):
    record.append([input(), float(input())])

record = sorted(record, key = lambda x: x[0])
secondLowest = sorted(set([i[1] for i in record]))[1]
for i in record:
    if i[1] == secondLowest:
        print(i[0])
