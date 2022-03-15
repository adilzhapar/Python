with open('input.txt', 'r') as f:
    x = f.read().split()

n = int(input())
txt = ""
for s in x:
    for i in s:
        txt += chr(ord(i)-n)
    txt += ' '

with open('output.txt', 'w') as r:
    r.write(txt)

# print(x)