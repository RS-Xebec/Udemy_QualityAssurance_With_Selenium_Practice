# Reading file from the file
# obj = open("D:\\UDEMY\\Py.txt.txt",'r')

#REad all the data from the file
# print(obj.read())   

#Read one line from the file
# print(obj.readline())
# print(obj.readline())

# Read only few characters from file
# print(obj.read(10))

#Read all character from the file and display one by one
# for i in obj.read():
#     print(i)

#Read all data from file line by line
# s=obj.readline()
# while(s):
#     print(s)
#     s=obj.readline()

#Writing data into the file When we use w it deletes the previous data and write the new one
# obj = open("D:\\UDEMY\\Py.txt.txt",'w')
# obj.write("Hello this is new Python file")
# obj.close()

#Appending data into the file When we use a, it appends the new data to the previous one
# obj = open("D:\\UDEMY\\Py.txt.txt",'a')
# obj.write("\nHello this is new appended python file\n")
# obj.close()


#tell() and seek()
obj = open("D:\\UDEMY\\Py.txt.txt",'r')
print("Current file pointer position:",obj.tell())
obj.read()
print("Current file pointer position:",obj.tell())
obj.read()
print(obj.tell())
obj.seek(5)
print("After seeking file pointer position:",obj.tell())
obj.close()