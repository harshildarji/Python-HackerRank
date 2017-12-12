# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

list = []
n = int(input().strip())

for i in range(0, n):
    command = input().split()
    if command[0] == 'insert':
        list.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(list)
    elif command[0] == 'remove':
        list.remove(int(command[1]))
    elif command[0] == 'append':
        list.append(int(command[1]))
    elif command[0] == 'sort':
        list.sort()
    elif command[0] == 'pop':
        list.pop()
    elif command[0] == 'reverse':
        list.reverse()
