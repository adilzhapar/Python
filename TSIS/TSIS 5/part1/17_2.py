with open('colors.txt', 'r') as f:
    x = [i.rstrip('\n') for i in f.readlines()]
print(x)
