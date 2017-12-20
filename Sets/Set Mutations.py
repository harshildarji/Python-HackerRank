# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input().strip())
A = set([int(i) for i in input().split()][:n])
N = int(input().strip())
for i in range(N):
    com = input().split()
    values = set([int(i) for i in input().split()][:int(com[1])])
    exec('A.' + com[0] + '(values)')
print(sum(A))
