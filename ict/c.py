from math import sqrt
a, b, c = map(int, input().split())
x1 = (-b + sqrt(b**2 - 4 * a * c)) / 2*a
x2 = (-b - sqrt(b**2 - 4 * a * c)) / 2*a

print(x1, x2)
