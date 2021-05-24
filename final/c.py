arr = list(map(int, input().split()))

for i in arr:
    if i == 0:
        arr.remove(0)
        arr.append(0)
print(*arr)