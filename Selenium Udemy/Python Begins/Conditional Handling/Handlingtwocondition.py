#Take input from user - number
#Check if this number is Even, Print this is even number
#Number is not Even, Print Odd Number
#Don't do anything if number is odd 

data = input("Please Enter your number: ")
data = int(data)

# Handling Condition now
if (data % 2 ==0):
    print("This is even number " + str(data))
else:
    print("This is odd number " + str(data)) 