handler = open('input.txt', 'r')
txt = handler.read().split()
txt.sort()
# print(txt)
mydict = {}
for i in txt:
    if i in mydict:
        mydict.update({i: int(mydict[i]) + 1})
    else: 
        mydict[i] = 1

for i in mydict:
    if int(mydict[i]) % 2 == 0:
        print(i)
