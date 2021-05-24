n = int(input())
md = {}
overall = 0

for i in range(n):
    name, score = input().split()
    overall += int(score)
    if name not in md:
        md[name] = int(score)
    else:
        md[name] += int(score)
for i in md:
    # x = "{:.4f}".format(md[i] / overall * 100)
    x = md[i] / overall * 100
    if x.is_integer():
        md[i] = int(x)
    else:
        md[i] = float("{:.4f}".format(md[i] / overall * 100))


md = dict(sorted(md.items(), key=lambda x: x[1], reverse=True))

for i in md:
    print(i, str(md[i])+'%')