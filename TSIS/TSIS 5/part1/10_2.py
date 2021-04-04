# count number of each word
from collections import Counter
with open("input.txt", 'r') as f:
    dict = Counter(f.read().split())
print(dict)