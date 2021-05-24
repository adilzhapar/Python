n = int(input())
arr = []

for i in range(n):
    arr.append([j+i for j in range(n)])


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()