# Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

string = list(input().strip())
change = input().strip().split()
string[int(change[0])] = change[1]
print("".join(string))
