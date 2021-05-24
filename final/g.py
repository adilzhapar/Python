import string

s = input().split()
res = dict().fromkeys(string.ascii_lowercase, 0)
for i in s:
    res[i[0].lower()] += 1
for i in res.values():
    print(i)