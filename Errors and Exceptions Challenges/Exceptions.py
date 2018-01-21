# Exceptions
# https://www.hackerrank.com/challenges/exceptions/problem

r = []
for _ in range(int(input().strip())):
    try:
        a, b = map(int, input().split())
        r.append(a//b)
    except ZeroDivisionError as e:
        r.append('Error Code: ' + str(e))
    except ValueError as e:
        r.append('Error Code: ' + str(e))
print(*r, sep = '\n')
