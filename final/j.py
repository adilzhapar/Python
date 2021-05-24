def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n == 0 or n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())

for i in range(b, a-1, -1):
    if isPrime(i):
        print(i, end=' ')