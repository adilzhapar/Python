a, b, k = map(int, input().split())
arr = []


def isDivide(a, b, arr):
    x = min(a, b)
    for i in range(1, x+1):
        if a % i == 0 and b % i == 0:
            arr.append(i)
    return arr


arr = isDivide(a, b, arr)
arr.sort(reverse=True)
print(arr[k-1])