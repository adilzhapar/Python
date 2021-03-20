n = int(input("input N: "))
m = int(input("input M: "))
num = int(input("input n: "))

def Factorial(n, res):
    if n == 0:
        return res
    else:
        return Factorial(n-1, res) * n


def Comb(n, m):
    return int(Factorial(n, 1) / (Factorial(m, 1) * Factorial(n-m, 1)))


def Result(i):
    return float(Comb(m, i) * Comb(n-m, num-i) / Comb(n, num))


for i in range(num+1):
    print(float("{:.4f}".format(Result(i))))
# print(Comb(n, num))
