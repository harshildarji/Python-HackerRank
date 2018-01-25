# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem

import string

print(*sorted(input().strip(), key = (string.ascii_letters + '1357902468').index), sep = '')
