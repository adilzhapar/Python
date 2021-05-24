my_set = set(input().split())
last = []
for i in my_set:
    if i != i[::-1]:
        last.append(i)

last.sort()
for i in last:
    print(i)
