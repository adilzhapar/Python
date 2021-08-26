arr = list(map(int, input().split()))
sum = 0
my_dic = {}
for i in arr:
    if i not in my_dic:
        my_dic[i] = 0
    my_dic[i] += 1
for i, j in my_dic.items():
    if j == 1:
        sum += i

print(sum)
