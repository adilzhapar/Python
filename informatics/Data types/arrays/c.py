a = set(map(int, input().split()))
b = set(map(int, input().split()))
a.intersection(b)
a.intersection_update(b)

for i in a:
    print(i, end=' ')
