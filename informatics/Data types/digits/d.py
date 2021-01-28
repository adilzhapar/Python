k, n = map(int, input().split())

if k >= n:
    print("{} {}".format(n, n))
    exit()

cnt=1

while(True):
    cnt += 1
    n -= k
    if(n <= k):
        print("{} {}".format(cnt, n))
        break
    else:
        continue
