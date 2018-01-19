# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

d, m, y = map(int, input().split())

days = list(calendar.day_name)
print(days[calendar.weekday(y, d, m)].upper())
