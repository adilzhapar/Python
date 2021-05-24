a, b = map(int, input().split())
c, d = map(int, input().split())

if a + d > b + c:
    print("Barsenal")
elif a + d < b + c:
    print("Arselona")
else:
    if b > d:
        print("Arselona")
    elif b < d:
        print("Barsenal")
    else:
        print("Friendship")
print(a+d, b+c)
