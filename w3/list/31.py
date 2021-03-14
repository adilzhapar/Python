my_list = list(map(int, input().split()))
m, n = map(int, input().split())
for i in my_list:
    if i in range(m, n):
        print(i)