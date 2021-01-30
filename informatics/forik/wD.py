n = int(input())
bin = ""

while n != 0:
    bin += str(n%2)
    n = int(n / 2)

print(bin)
