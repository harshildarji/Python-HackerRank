# Write a function
# https://www.hackerrank.com/challenges/write-a-function/problem

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
        
if __name__ == '__main__':
    year = int(input().strip())
    print(isLeap(year))
