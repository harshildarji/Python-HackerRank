# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

s = [i for i in input()]
n = int(input().strip())
for i in range(0, len(s), n):
    string = s[i:i+n]
    word = ""
    for w in string:
        if w not in word:
            word += w
    print(word)
