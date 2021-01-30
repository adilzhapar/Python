n = int(input())
myset = set()
mylist = []

for i in range(n):
    try:
        command, num = input().split()
    except ValueError:
        command = "COUNT"
    if command == "ADD":
        myset.add(int(num))
    elif command == "PRESENT":
        if int(num) in myset:
            mylist.append("YES")
        else:
            mylist.append("NO")
    else:
        mylist.append(len(myset))

for i in mylist:
    print(i)
