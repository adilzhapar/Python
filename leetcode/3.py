s = input()
s = list(s)
if(len(s) == 1):
    print(1)
    exit()
ss = list()
max = 0
for i in s:
    if len(ss) == 0:
        ss.append(i)
    elif i in ss:
        if len(ss) > max:
            max = len(ss)
        ss.clear()
        ss.append(i)
    else:
        ss.append(i)
        if len(ss) > max:
            max = len(ss)
print(max)
