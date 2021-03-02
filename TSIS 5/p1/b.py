# первые n строк
n = int(input())
f = open("input.txt", 'r')

k = 0
for i in f:
    if k < n:
        print(i)
        k += 1
    else: break 