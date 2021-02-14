import json
f = open("data.json",)

def withdis(x, d):
    ans = int(int(x) * (100-int(d)) / 100)
    return ans


my_dict = json.load(f)
min = 1000
for i in my_dict['Subscriptions']:
    x = withdis(i['price'], i['discount'])
    if x < min:
        min = x

for i in my_dict['Subscriptions']:
    if min == int(i['price']):
        print('Name:', i['name'])
        print('Price:', i['price'])
f.close()

    
