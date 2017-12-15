# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import sys,string
n=int(input().strip())
w=2*n-1
s=string.ascii_lowercase[:n][::-1]
for _ in range(w):
    i=min(_,w-_-1)
    print('-'*(w-2*i-1)+'-'.join(list(s[:i]+s[i]+s[:i][::-1]))+'-'*(w-2*i-1))
