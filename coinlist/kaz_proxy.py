import csv
with open('kaz_proxy.txt', 'r') as f:
    x = f.read().split('\n')
    
x = list(map(lambda x: x.replace('\t', ':'), x))
print(*x, sep='\n')
n = open('final_kaz.txt', 'w')

for i in x:
    n.write(i + '\n')

n.close()