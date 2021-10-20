import re
import csv
pr = []

def Convert(string):
    li = list(string.split(":"))
    return li

with open('proxy.txt', 'r') as f:
    pr = f.readlines()
# print(*pr, sep='\n')
for i in range(len(pr)):
    pr[i] = Convert(pr[i])
# for i in pr:
    # print(*i)
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(pr)