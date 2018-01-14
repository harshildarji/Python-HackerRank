# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

r = []
for _ in range(int(input().strip())):
    n = int(input().strip())
    l = list(map(int, input().split()))[:n]
    
    left, right = 0, n - 1

    top = -1
    failed = False
    while right - left > 0 and failed == False:
        if l[left] > l[right]:
            if top >= l[left] or top == -1:
                top = l[left]
                left += 1
            else: failed = True
        else:
            if top >= l[right] or top == -1:
                top = l[right]
                right -= 1
            else: failed = True
    r.append("No" if failed else "Yes")
print(*r, sep = '\n')
