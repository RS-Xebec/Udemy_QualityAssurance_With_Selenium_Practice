a= "Hello"
b= "Hello"

if (a==b):
    print("Strings are same")

else:
    print("Strings are not same")
#This is case sensative comparision


a= "   Hello"
b= "Hello   "

if (a.strip()==b.strip()):
    print("Strings are same")

else:
    print("Strings are not same")

#These all are case sensative comparision
#Now for doing case insensative comparision
a= "Hello"
b= "hello"
if(a.upper()==b.upper()):
    print("Strings are same by applying case insensative")

else:
    print("Strings aren't same by applying case insensative")
