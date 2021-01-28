try:
    s = list(map(int, input().split('.')))
except ValueError:
    print(0)
    exit(0)

if len(s) > 4:
    print(0)
else:
        print(1)
