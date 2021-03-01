import csv

with open('ex2.csv') as f:
    reader = csv.reader(f, delimiter=',')
    line = 0
    for r in reader:
        print(r[0], r[1], r[2])