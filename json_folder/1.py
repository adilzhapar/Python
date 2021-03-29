import json
import csv
with open('AD_03.json', 'r', encoding='utf8') as f:
    x = f.read()
y = json.loads(x)
# print(type(y))
# print(type(y[0]))
# for i in y:
#     print(i.items())
my_dict = {}
for i in range(0, len(y), 2):
    my_dict[y[i].values()] = y[i+1].values()
    
for i, j in zip(my_dict.keys(), my_dict.values()):
    print(i, j)


# with open('file.csv', 'w', encoding='utf8', newline='') as output_file:
#     fc = csv.DictWriter(output_file, 
#                         fieldnames=y[0].keys(),
#                        )
#     fc.writeheader()
#     fc.writerows(y)