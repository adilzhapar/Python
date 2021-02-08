arr = list(map(str, input().split()))
max = 0

for i in arr:
    if len(i) > max:
        max = len(i)
        s = i
print(i)
print(max)