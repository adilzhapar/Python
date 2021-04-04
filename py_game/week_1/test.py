nums = ['0.00', '0.25', '0.50', '0.75', '1.00']
nums.remove('0.00')
myiter = iter(list(map(lambda x: '-' + x, nums)))
for i in range(4):
    print(next(myiter))
print('-----')
print(chr(960))
