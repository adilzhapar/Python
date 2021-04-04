from itertools import islice
n = int(input())
file = open("input.txt", 'r')
for line in islice(file, n):
    print(line)