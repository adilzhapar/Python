def is_three(n):
    while n % 3 == 0:
        n /= 3
    return n == 1


a, b = map(int, input().split())

for i in range(b, a, -1):
    if is_three(i) and i // 1000 > 0 and i // 1000 < 10:
        print(i, end=' ')