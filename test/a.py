
with open("input.txt", 'r', encoding='utf8') as f:
    l = f.readlines()
# print(*l, end='\n')

for i in range(len(l)):
    if(l[i].strip()[0:3] == '$$$'):
        l[i] =  l[i][3:]
    elif(l[i].strip()[0:2] == '$$'):
        l[i] = '+ ' + l[i][2:]
    elif(l[i].strip()[0:1] == '$'):
        l[i] = '- ' + l[i][1:]

with open('output.txt', 'w', encoding='utf8') as f:
    f.writelines(l)