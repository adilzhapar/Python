multiple = []
variants = []
frequency = []
z = int(input('number of measurments: '))
for i in range(z):
    x, n = map(float, input('input variant(x) and frequency(n) ').split())
    multiple.append(float(x*n))
    variants.append(x)
    frequency.append(n)
value = float("{:.2f}".format(sum(multiple) / sum(frequency)))

print('Sum of x*n', sum(multiple))
print('Sum of n\'s', sum(frequency))
print('Arithmetic mean is: ', value)

delta_square = [float("{:.2f}".format(abs(i-value)**2 * j)) for i, j in zip(variants, frequency)]
print(*delta_square)
print("Sum of (x-x_)^2 * n: ", "{:.3f}".format(sum(delta_square)))
