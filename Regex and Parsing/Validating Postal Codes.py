# Validating Postal Codes
# https://www.hackerrank.com/challenges/validating-postalcode/problem

import re

print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))
