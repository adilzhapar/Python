l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

x = 0
y = 0
dec = 1

for i in l1:
    x += i * dec
    dec *= 10

dec = 1

for i in l2:
    y += i * dec
    dec *= 10

c = x + y
last = []
while c != 0:
    last.append(c%10)
    c //= 10
print(last)