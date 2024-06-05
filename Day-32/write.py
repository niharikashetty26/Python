file = open('test.txt', 'w')
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file")
file.close()

file=open("test.txt","r")
print(file.read())