n = int(input())
arr = list(map(int, input().split()))

x = max(arr)

for i in arr:
    if i == x:
        print(1, end=' ')
    else:
        print(0, end=' ')