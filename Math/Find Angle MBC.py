# Find Angle MBC
# https://www.hackerrank.com/challenges/find-angle/problem

import math

AB = int(input().strip())
BC = int(input().strip())
print(str(round(math.degrees(math.atan2(AB, BC)))) + '°')
