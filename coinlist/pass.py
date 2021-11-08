# Password generator
from random import randrange, randint
letters = [chr(i) for i in range(97, 123)]
print(*letters)
big_letters = [chr(i) for i in range(65, 91)]
print(*big_letters)
nums = [chr(i) for i in range(48, 58)]
print(*nums)
s = ''.join(letters[randint():5]+big_letters[5:6]+nums[:-1])
print(s)