arr = list(input().split())

md = {}
for i in arr:
    if i not in md:
        md[i] = 1
    else:
        md[i] += 1

md = dict(sorted(md.items(), key=lambda x: x[0]))

for i, j in zip(md.keys(), md.values()):
    print(i, j)