import re
txt = input()
t = ''
for i in txt:
    if i.isalpha():
        t += i.lower()
    else:
        t += i
x = re.search(r'^(PP2|pp2).*midterm$', t)
print('Success' if x else 'No')