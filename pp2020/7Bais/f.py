k = int(input())
s = input()
s = list(s)

for i in s:
    if ord(i) + k > 90:
        print(chr(ord(i) + k - 26), end='')
    else:
        print(chr(ord(i) + k), end='')

# for i in s:
#     print(ord(i))
#     print(ord(i) + k - 25)