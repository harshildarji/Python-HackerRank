# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

n = int(input().strip())
width = len("{0:b}".format(n))
for i in range(1, n + 1):
    line = "{0}".format(i).rjust(width) 
    line += " " + "{0:o}".format(i).upper().rjust(width)
    line += " " + "{0:x}".format(i).upper().rjust(width)
    line += " " + "{0:b}".format(i).upper().rjust(width)
    print(line)
