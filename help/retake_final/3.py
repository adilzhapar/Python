name = input()
with open('output.txt', 'w') as f:
    f.write('Hi, {}'.format(name))
    f.close()