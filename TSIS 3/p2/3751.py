print(*sorted(set(set(map(int, input().split()))) & set(map(int, input().split())), key=int))
