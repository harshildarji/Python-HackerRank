# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input().strip())
record = dict()

for i in range(n):
    line = input()
    lst = line.split()
    record[lst[0].title()] = [float(i) for i in lst[1:]]

name = input().title()
if name in record:
    marks = record[name]
    print("%.2f" % float(sum(marks)/len(marks)))
    
