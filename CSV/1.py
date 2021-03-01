import csv
#read csv
with open('w5.csv') as f:
    reader = csv.reader(f, delimiter=',')
    line = 0
    for row in reader:
        print(row[0], row[1], row[2])
