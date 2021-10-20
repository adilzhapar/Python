# find max:
a = list(map(int, input().split()))

max = a[0]
for i in a:
    if i > max:
        max = i
print(max)

# sum of remainders
sum = 0
for i in a:
    sum += (i % max)
print(sum)

# sort by ascending order of remainders:
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if(a[i] % max > a[j] % max):
            a[i], a[j] = a[j], a[i]
print(*a)
