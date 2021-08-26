n = int(input())
final = []
for i in range(n):
    arr = list(input().split())
    final.append([len(i) for i in arr])
for arr in final:
    print(*sorted(arr), 'total:', sum(arr))
    