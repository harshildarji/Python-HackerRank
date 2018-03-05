# Validating and Parsing Email Addresses
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
for _ in range(int(input().strip())):
    s = input()
    m = re.match(r'.*?\<([a-z]+[a-z0-9_\.\-]+)@([a-z]+)\.([a-z]{1,3})\>.*?', s)
    if m is not None and len(m.groups()) == 3:
        print(s)
