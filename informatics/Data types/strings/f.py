words = list(map(str, input().split()))

a = ""

for i in words:
    if len(i) > len(a):
        a = i

print(a)
print(len(a))