# Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
        
