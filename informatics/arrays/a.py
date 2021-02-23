s = int(input())
a = list(map(int, input().split()))
for i in range(1, len(a), 2):
    print(a[i], end=' ')
    