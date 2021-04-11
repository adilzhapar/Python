
with open('text.txt', 'r') as f:
    my_list = map(int, f.read().split(', '))
# print(*my_list)
my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

print(*sorted(my_dict.items()))
sum = 0
for i in my_dict.values():
    sum += i
print(sum)
