n = int(input())
zero = 0
plus = 0
minus = 0

for i in range(n):
    a = int(input())
    if a == 0:
        zero += 1
    elif a > 0:
        plus += 1
    else:
        minus += 1
    
print(zero, plus, minus)