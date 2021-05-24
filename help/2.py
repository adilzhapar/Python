def unique(arr):
    my_set = set()  # создаю сет (уникальные числа хранятся в сете)
    for i in arr:
        if i not in my_set:  # если i-тое число не в сете, добавляю в сет
            my_set.add(i)
        else:  # иначе, оно встречается во второй раз, возвращаем это число
            return i
