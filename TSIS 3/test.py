arr = list(map(int, input().split()))
k = int(input())
if k > 0:
    a = int(len(arr) - k)
    arr = arr[a:] + arr[:a]
else:
    k = int(abs(k))
    arr = arr[k:] + arr[:k]
for i in arr:
    print(i, end=' ')

