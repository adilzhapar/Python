n, k = map(int,input().split())
coins = list(map(int, input().split()))
for i in range(len(coins)):
    for j in range(i, len(coins)):
        if i != j and coins[i] + coins[j] == k:
            print("Bon Appetit")
            exit()

print("So sad")