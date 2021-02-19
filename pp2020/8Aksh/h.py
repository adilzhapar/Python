# trib = lambda x: x = 1 if x <= 2 and x > 0 else trib(x-3) + trib(x-2) + trib(x-1)

def Trib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return (Trib(n-3) +
                Trib(n-2) + 
                Trib(n-1))

n = int(input())
print(Trib(n))
