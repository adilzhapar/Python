s = input()
my_dict = {}

for i in s:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

print(len(my_dict))
my_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
for i in my_dict:
    print(i, my_dict[i])