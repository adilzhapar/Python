a, b = map(int, input().split())
busy = list(map(int, input().split()))
print(*[i for i in range(a, b+1) if i not in busy])