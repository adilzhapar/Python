a = []
for i in range(11):
    a.append(['*' for j in range(13)])
s = 5
for i in range(4, 11):
    for j in range(-s):
        a[i][j] = ' '
        s -= 1

        
for i in a:
    for j in i:
        print(j, end=' ')
    print()