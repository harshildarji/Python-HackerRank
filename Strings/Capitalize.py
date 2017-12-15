# Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

input = input().split(" ")
output = []

for word in input:
    if word:
        output.append(word[0].upper() + word[1:].lower())
    else:
        output.append("")

print(" ".join(output))
