def Factorial(n, res):
    if n == 0:
        return res
    else:
        return Factorial(n-1, res) * n


n = int(input("Input n: "))
m = int(input("Input m: "))

a = Factorial(n, 1)
b = Factorial(n-m, 1)
print("A is:", int(a / b))