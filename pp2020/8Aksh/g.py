
n = int(input())

while n > 0:
    if n % 7 == 0 or n % 4 == 0 or n % 11 == 0:
        print("yes")
        exit()
    n -= 4
print("no")
