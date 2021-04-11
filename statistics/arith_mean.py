multiple = []
frequency = []
z = int(input('number of measurments: '))
for i in range(z):
    x, n = map(float, input('input variant(x) and frequency(n) ').split())
    multiple.append(float(x*n))
    frequency.append(n)
value = sum(multiple) / sum(frequency)
print('Sum of x*n', sum(multiple))
print('Sum of n\'s', sum(frequency))
print('Arithmetic mean is: ', f'{value:.3f}')


