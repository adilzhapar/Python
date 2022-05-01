
with open("input.txt", 'r', encoding='utf8') as f:
    l = f.readlines()
# print(*l, end='\n')

for i in range(len(l)):
    if l[i][0].isdigit():
        cnt = 0
        while(l[i][cnt].isdigit()):
            cnt += 1
        l[i] = l[i][cnt:]
        cnt = 0
    if l[i][0:2] == "а)":
        l[i] = "+ " + l[i][2:]
    elif l[i][0:2] == "b)":
        l[i] = "- " + l[i][2:]
    elif l[i][0:2] == "c)":
        l[i] = "- " + l[i][2:]
    elif l[i][0:2] == "d)":
        l[i] = "- " + l[i][2:] + '\n'



with open('output.txt', 'w', encoding='utf8') as f:
    f.writelines(l)