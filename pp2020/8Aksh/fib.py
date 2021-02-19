fib = lambda x: x if x <= 1 else fib(x-2) + fib(x-1)
print(fib(int(input())))