# Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
s = input()
n = int(input().strip())
print(textwrap.fill(s, n))
