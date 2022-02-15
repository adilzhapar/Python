d = {
    ('Adil', 'Zhapar'): '20B8712398123',
    ('Asdfasdf', 'Vcxvb'): '19B8712398123',
    ('Gjosdufjlas', 'Zhapazxcvzxvr'): '20B8712398123',
    ('Ernat', 'Zhapar'): '18B8712398123',
}

ss = list(d)
ss.sort(key=lambda x: x[1])

arr = [int(i) for i in input().split()]
print(*arr)