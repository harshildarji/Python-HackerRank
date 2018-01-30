# Re.split()
# https://www.hackerrank.com/challenges/re-split/problem

import re
for i in re.split('[, .]', input().strip()):
    if i.isdigit(): print(i)
