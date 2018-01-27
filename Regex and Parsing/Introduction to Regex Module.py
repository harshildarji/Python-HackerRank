# Introduction to Regex Module
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re
r = []
for _ in range(int(input().strip())):
    r.append(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input().strip())))
print(*r, sep = '\n')
