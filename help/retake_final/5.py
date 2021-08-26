arr = list(map(int, input().split()))
cnt = 0
for i in range(len(arr)):
    for j in range(1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
print(cnt-1)