import requests
with open("output.txt", 'w') as f:
    for i in range(22500, 25000):
        s = f"http://78.140.223.58/problems/contest-{i}-en.pdf"
        res = requests.get(s)
        print(i, end=' ')
        if res.ok:
            f.write(s + '\n')
        else:
            print("shit")
f.close()