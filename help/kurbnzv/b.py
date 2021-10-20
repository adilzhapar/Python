
a = list(map(int, input().split()))

# find minimum:
min = a[0]
for i in a:
    if i <= min:
        min = i
print(min)

# sum between positives
test = False
sum = 0
for i in range(len(a)):
    if a[i] > 0:
        while a[i] > 0:
            sum += a[i]
            i += 1
        break
print(sum)

# 0's first:
cnt = 0
ll = []
for i in a:
    if i == 0:
        cnt += 1
    else:
        ll += [i]
print('0 ' * cnt, end='')
print(*ll) 