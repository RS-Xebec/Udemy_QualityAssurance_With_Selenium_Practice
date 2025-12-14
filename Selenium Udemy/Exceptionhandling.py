# #While executing a code if we get error in runtime , this type of error is called runtime error or logical error or exception

# #Task we want to perform in case of getting exception is called exception handling


# #Exception handling in python is done by using try, except and finally

# user_input1= input("Enter first number: ")
# user_input2= input("Enter second number: ")
# c = int(user_input1) + int(user_input2)
# print("The addition is:",c)

# try:
#     user_input1= input("Enter first number: ")     #put alphanumeric value like 3a or 4d to get exception
#     user_input2= input("Enter second number: ")
#     c = int(user_input1) + int(user_input2)
#     print("The addition is:",c)

# except:
#     print("Your input is incorrect, please enter numeric value only")

# #Now whether you have an exception in your code or not , finally block will always execute and it is written after try and except not before that and it is also not mandatory to write finally block

# #finally is used to execute a code whether an exception occurs or not

# finally:
#     print("This code is always i want to execute always at the end") 


from configparser import ConfigParser

#Created  object of ConfigParser class
config =ConfigParser()

#To read data from config file
config.read("./Inputfiles/config.cfg")

print(config.get("Section1","username"))