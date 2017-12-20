# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input().strip())
rooms = list(map(int, input().split()))
print(int((sum(set(rooms)) * k - sum(rooms)) / (k - 1)))
