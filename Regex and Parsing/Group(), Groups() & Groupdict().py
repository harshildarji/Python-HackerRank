# Group(), Groups() & Groupdict()
# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

s = re.search(r'(?!_)(\d|\w)\1', input())
print('-1' if s is None else s.group(0)[0])
