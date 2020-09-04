if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi=max(arr)
    for i in arr[::-1]:
        if i!=maxi:
            print(i)
            break


