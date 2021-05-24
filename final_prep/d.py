l, r = map(int, input().split())

# for i in range(l, r+1):
#     if i % 2 == 1:
#         print(i, end=' ')

def Odd(l, r):
    if l == r:
        if l % 2 == 1:
            print(l, end=' ')
            return
        else: return
    if l % 2 == 1:
        print(l, end=' ')
    Odd(l+1, r)

Odd(l, r)