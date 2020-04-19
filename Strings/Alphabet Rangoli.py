# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string
def print_rangoli(size):
    w=2*size-1
    s=string.ascii_lowercase[:size][::-1]
    for _ in range(w):
        i=min(_,w-_-1)
        print('-'*(w-2*i-1)+'-'.join(list(s[:i]+s[i]+s[:i][::-1]))+'-'*(w-2*i-1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
