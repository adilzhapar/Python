s = list(map(str, input().split()))
names = {}
for i in s:
    if i not in names:
       names[i] = 0
    names[i] += 1
names = dict(sorted(names.items(), key=lambda x: x[0]))
for i, j in names.items():
    print('{} - {}'.format(i, j)) 