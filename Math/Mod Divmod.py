# Mod Divmod
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

m, n = int(input().strip()), int(input().strip())
print('%d\n%d\n%s' % (m//n, m%n, divmod(m, n)))
