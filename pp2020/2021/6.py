vowels = ['a', 'e', 'i', 'o', 'y', 'u']
my_dict = {"a":0, "b":0, "c":0}
n = int(input())
for i in range(n):
    a, b, c = input().split()
    for j in a:
        if j.isupper():
            my_dict["a"] += 1
    for k in b.lower():
        if k in vowels:
            my_dict["b"] += 1
    for m in c:
        if m.isdigit():
            my_dict['c'] += 1
print(*my_dict.items())