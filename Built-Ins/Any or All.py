# Any or All
# https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input().strip())
a = list(map(int, input().split()))[:n]
print(True if all(i > 0 for i in a) and any(str(i) == str(i)[::-1] for i in a) else False)
