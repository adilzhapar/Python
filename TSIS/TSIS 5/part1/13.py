#copy file
address = input("input the name of file witout .txt: ")
handler = open(address + ".txt", 'r')
txt = handler.read()
new = open(address + "(1)" + ".txt", 'w')
new.write(txt)
