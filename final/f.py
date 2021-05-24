my_set = set(map(int, input().split()))

def is_two(n):
    while n % 2 == 0:
        n /= 2
    return n == 1

last = []
for i in my_set:
    if not is_two(i):
        last.append(i)
print(*last)