# Regex Substitution
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

for i in range(int(input().strip())):
    print(re.sub(r'(?<= )\|\|(?= )', 'or', re.sub(r'(?<= )&&(?= )', 'and', input())))
