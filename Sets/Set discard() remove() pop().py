# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input().strip())
values = set([int(i) for i in input().split()][:n])
ops = int(input().strip())
for i in range(ops):
    op = input().split()
    if op[0] == 'pop':
        values.pop()
    elif op[0] == 'remove':
        values.remove(int(op[1]))
    elif op[0] == 'discard':
        values.discard(int(op[1]))
print(sum(values))
