def move(s):
    x, y = 0, 0  # начальные координаты робота
    for i in s:  # координаты меняются:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'L':
            x -= 1
        else:
            x += 1
    return x == 0 and y == 0  # если x, y снова равны нулю, значит True


