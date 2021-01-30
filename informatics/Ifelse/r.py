k = int(input())
m = int(input())
n = int(input())

time = 0

if k >= n:
    print(2*m)
    exit()
else:
    while n >= k:
        time += m*2
        n -= k

time += m*2
print(time)
