# Validating Email Addresses With a Filter
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

addr = re.compile('''^[\w-]{1,}@[a-zA-Z0-9]{1,}\.\w{1,3}$''', re.UNICODE | re.VERBOSE)
print(sorted(filter(addr.search, (input() for _ in range(int(input()))))))
