a = int(input())
b = int(input())
c = int(input())
d = int(input())


def Polynomial(x):
    return a * x**3 + b * x**2 + c * x + d == 0


arr = []
for i in range(1001):
    if Polynomial(i):
        arr.append(i)

for i in arr:
    print(i, end=" ")