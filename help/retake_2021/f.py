import re

log = input()
pas = input()

x = re.search(r'\w{3,32}#\d{4}', log)
y = re.search(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d][A-Za-z\d!@#$%^&*()_+]{8,}$', pas)
if x and y:
    print("Welcome to Discord")
else:
    print("Invalid password or username")