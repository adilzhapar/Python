from math import *
with open('text.txt', 'r') as f:
    my_list = map(float, f.read().split(', '))
# print(*my_list)
my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
print('x-s: ', len(my_dict))
print(*sorted(my_dict.items()))
sum = 0
for i in my_dict.values():
    sum += i
print('n-s:', sum)

xn = 0
for i, j in zip(my_dict.keys(), my_dict.values()):
    xn += i * j
print(xn)
mean = float(xn / sum)
mean = f'{mean:.3f}'
print('Arithmetic mean: ', mean)
deviation = 0
for i, j in zip(my_dict.keys(), my_dict.values()):
        deviation += abs(i - float(mean))**2 * j
print(deviation)
print('Deviation: ', deviation / sum)