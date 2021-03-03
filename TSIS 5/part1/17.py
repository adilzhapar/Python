#убрать "новые строки"
with open('colors.txt', 'r') as f:
    x = f.read().splitlines()
print(*x)