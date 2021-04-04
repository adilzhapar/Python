s = input()
if s == s[::-1]:
    print(s)
max = 0
ss = ""
for i in range(0, len(s)):
    for j in range(i, len(s)+1):
        nex = s[i:j]
        # print(i, j, nex)
        if nex == nex[::-1] and len(nex) > max:
            max = len(nex)
            ss = nex

print(ss) 
