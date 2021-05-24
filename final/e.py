given = list(map(int, input().split()))
my_dict = {}
last = []

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n == 0 or n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


for i in given:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for i in my_dict:
    if my_dict[i] > 1 and isPrime(i) is False:
        last.append(i)
print(*last)



