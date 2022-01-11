import re
import csv
pr = []

def Convert(string):
    # li = list(string.split(":"))
    return re.split(r':|@', string)
    

with open('newproxy.txt', 'r') as f:
    pr = f.readlines()

# print(*pr)
pr.reverse()
for i in range(len(pr)):
    pr[i] = Convert(pr[i])
    print(pr[i])

cnt = 0 
for i in pr:
    cnt += 1
print(cnt)
with open('file_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(pr) 