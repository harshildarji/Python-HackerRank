# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input().strip())
countries = set()
for i in range(n):
    countries.add(input().strip())
print(len(countries))
