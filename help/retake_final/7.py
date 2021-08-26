n = int(input())
my_dic = {}
for i in range(n):
    arr = list(input().split())
    if arr[0] not in my_dic:
        my_dic[arr[0]] = []
    my_dic[arr[0]] += arr[1:]
for i, j in my_dic.items():
    print(i + ':', ', '.join(j))