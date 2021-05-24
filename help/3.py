# считываю необходимые данные:
a = int(input())
b = int(input())
h = int(input())

try:  # пытаюсь найти площадь:
    s = (a+b)/2 * h
    print(s)
except:  # иначе пропускаю
    pass