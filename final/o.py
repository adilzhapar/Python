words = list(map(lambda a: a.upper(), input().split()))

md = {}
for i in words:
    if i not in md:
        md[i] = 1
    else:
        md[i] += 1
md = dict(sorted(md.items(), key=lambda x: x[1], reverse=True))

for i in md.keys():
    print(i)
    break
