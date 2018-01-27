# Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print(list(map(lambda x: x**3, map(fib, range(int(input().strip()))))))
