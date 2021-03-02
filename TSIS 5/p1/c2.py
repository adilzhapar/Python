with open("text.txt", "w") as handler:
    handler.write("Some new words:\n")
    handler.write("Python is cool")
print(handler.read())