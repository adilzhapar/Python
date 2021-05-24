s = input()
l = ""

for i in s:
    if i not in l:
        l += i
print(l)
