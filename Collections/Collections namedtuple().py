# Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

n = int(input().strip())
student = __import__('collections').namedtuple('student', input().strip())
std = [student(*input().split()) for _ in range(n)]
print(sum(float(s.MARKS) for s in std)/n)
