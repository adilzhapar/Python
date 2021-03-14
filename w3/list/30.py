my_list = list(map(int, input().split()))
my_dict = dict()
for i in my_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
print(*my_dict.items())
