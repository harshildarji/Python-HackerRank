# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem
 
results = []
for i in range(int(input().strip())):
    a = int(input().strip()); A = set([int(i) for i in input().split()][:a]); b = int(input().strip()); B = set([int(i) for i in input().split()][:b]); results.append(A < B)
print(*results, sep = '\n')
