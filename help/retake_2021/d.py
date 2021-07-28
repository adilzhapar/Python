n = int(input())

def iscorrect(*arr):
    if len(arr) % 2 != 0:
        return False
    if not arr[0][0].isupper() and not arr[0][1:-1].islower():
        return False
    if arr[-1][-2:] != '33':
        return False
    for i in range(arr):
        if i % 2 == 0 and len(arr[i]) % 2 != 0:
            continue
        elif i % 2 != 0 and len(arr[i]) % 2 == 0:
            continue
        else:
            return False
    return True


results = []
for i in range(n):
    arr = input().split()
    if iscorrect(arr):
        results.append("Wow! That is perfect")
    else:
        results.append("Seriously?")

print(*results, sep='\n')