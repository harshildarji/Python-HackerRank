# Find a string
# https://www.hackerrank.com/challenges/find-a-string/problem

string = input().strip()
substring = input().strip()
count = 0
for i in range(0, len(string)):
    if string[i:i + len(substring)] == substring:
        count += 1
print(count)
        
