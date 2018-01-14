# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input().strip())).most_common(3)]
