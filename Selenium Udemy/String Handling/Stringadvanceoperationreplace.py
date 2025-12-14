#Advance String Operation
data = "Hello This is testing World IS"

print(data.replace("is","##"))
print(data.replace("World","Python"))
print(data.replace("l","L"))

#Replace "is" from your string with "$$$""
print(data.replace("is","$$$").replace("IS",("$$$")))


print(len(data))
print(len(data.replace(" ","")))


#FInd data in a string
print(data.find("This"))
print(data.find("Agile"))   #If the string is not found in the data it should return -1


#Split string on the behalf of space
result = (data.split(" "))
print(result)
print(len(result))
for data in result:
    print(data)


#Splitting on behalf of #
data = "Hello This is# testing World IS"
result = (data.split("#"))
print(result)
for data in result:
    print(data)