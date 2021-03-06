n = int(input())
if n == 1:
    s = int(input())
    print("Interesting")
    exit()
frozen = tuple(map(int, input().split()))
x = sorted(list(frozen))
if list(frozen) == x:
    print("Interesting")
else:
    print("Non interesting")