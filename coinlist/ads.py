import re
import csv
pr = []

def Convert(string):
    ll = re.split(r':|@', string)
    return ":".join(ll)

with open('newproxy.txt', 'r') as f:
    pr = f.readlines()


for i in range(len(pr)):
    pr[i] = Convert(pr[i])
    print(pr[i])
with open('file_3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(pr) 
