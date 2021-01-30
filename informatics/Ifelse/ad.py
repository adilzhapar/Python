naturals = []
decimals = []

for i in range(0, 3):
    naturals.append("I" * (i+1))
    decimals.append("X" * (i+1))
naturals.append("IV")
naturals.append("V")
decimals.append("XL")
decimals.append("L")

for i in range(5, 8):
    naturals.append("V" + naturals[i-5])
    decimals.append("L" + decimals[i-5])

naturals.append("IX")
# naturals.append("X")
decimals.append("XC")
decimals.append("C")

# print(naturals)
# print(decimals)

n = int(input())
a = n // 10
b = n % 10
if b != 0 and a != 0:
    print(decimals[a-1]+naturals[b-1])
elif a != 0:
    print(decimals[a-1])
else:
    print(naturals[b-1])

