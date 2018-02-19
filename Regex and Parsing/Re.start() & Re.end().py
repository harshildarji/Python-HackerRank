# Re.start() & Re.end()
# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re
s, a = [input() for i in '12']
[print('(%s, %s)' % (m.start(), m.end())) for m in re.finditer(a[:-1] + '(?=' + a[-1] + ')', s)] or print('(-1, -1)')
