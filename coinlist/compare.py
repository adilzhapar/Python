with open("test.txt", 'r') as f:
    x = f.read()

with open("test2.txt", 'r') as r:
    y = r.read()

print(x == y)