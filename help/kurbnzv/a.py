
a = [list(map(int, input().split())) for i in range(5)]

# finding k's:
for i in range(len(a)):
    second = [a[j][i] for j in range(5)]
    if a[i] == second:
        print(i)

# show sum if numbers are positive:
sum = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] >= 0:
            sum += a[i][j]
        else:
            sum = 0
            break
    if sum != 0:
        print(sum)
        sum = 0

