# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

r = []
for _ in range(int(input().strip())):
    line = input().strip()
    try:
        re.compile(line)
        r.append('True')
    except re.error:
        r.append('False')
print(*r, sep = '\n')
