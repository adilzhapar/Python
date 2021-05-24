n, m = map(int, input().split())
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

maks = 1
pos = 0

for i, j in enumerate(arr):
    if sum(j) > maks:
        maks = sum(j)
        pos = i+1
print(pos)