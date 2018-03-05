# Validating phone numbers
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
N = int(input().strip())
number = [input() for i in range(N)]
check = lambda no: len(re.findall('^[7-9]\d{9}$', no))
match = map(check, number)
for i in match:
    print('YES' if i == 1 else 'NO')
