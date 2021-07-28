n = int(input())
my_dict = {'a': 0,
           'b': 0,
           'c': 0}
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(n):
    a, b, c = input().split()
    for i in a:
        if i.isupper():
            my_dict['a'] += 1
    for i in b:
        if i in vowels:
            my_dict['b'] += 1
    for i in c:
        if i.isdigit():
            my_dict['c'] += 1

print(my_dict)