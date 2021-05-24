def zero(my_list):
    cnt = 0  # счетчик нулей
    for i in range(len(my_list)):
        if my_list[i] == 0:
            cnt += 1  # Пробежаться по листу, посчитать сколько раз встретился 0
    for i in range(cnt):
        my_list.remove(0)  # Удалить и добавить в конец 0, cnt раз
        my_list.append(0)
    return my_list



