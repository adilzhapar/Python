n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append([0 for j in range(m)])

for i in range(n // 2):
    for j in range(m // 2):
        arr[i][j] = 1

for i in range(n // 2, n):
    for j in range(m // 2):
        arr[i][j] = 2

for i in range(n // 2, n):
    for j in range(m // 2, m):
        arr[i][j] = 3

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()