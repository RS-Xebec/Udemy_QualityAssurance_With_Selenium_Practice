#Take input from user - number
#Check Number is Negative - Print this is Negative number
#Check number is Zero -Print its zero
#Check if it is positive, only then check even or odd

data = input("Please Enter your number: ")
data = int(data)

if data<0:
    print("This is Negative number....")
elif data==0:
    print("This is Zero.")
elif(data%2==0):
    print("This is even number")
else:                                    #else isn't mandatory we can also end condition wit elif
    print("This is odd number")