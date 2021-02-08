s = input()
n = int(input())
ss = ""
i = 0
l = len(s)
while l >= 0:
    ss += s[i:(n+n-2)]
    i = n + n -2
    l -= n + n -2
print(ss)
