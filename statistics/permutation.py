def Factorial(n, res):
    if n == 0:
        return res
    else:
        return Factorial(n-1, res) * n

n = int(input("Input n: "))
print("P is:", Factorial(n, 1))
