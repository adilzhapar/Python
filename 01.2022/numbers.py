from random import *
n = randint(1, 10)
res = False
for i in range(4):
    print("{} chance".format(i+1))
    x = int(input("Input your number:\n"))
    if x == n:
        print("Molodec!")
        res = True
        break
if res == False:
    print("lox")