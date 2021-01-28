arr = list(map(str, input().split()))
arr = "".join(arr)

if arr == arr[::-1]:
    print("yes")
else:
    print("no")

