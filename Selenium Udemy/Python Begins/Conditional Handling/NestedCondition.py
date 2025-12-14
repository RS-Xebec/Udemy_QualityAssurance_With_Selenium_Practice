# Take 1 input from user, check number is -ve or +ve
# - ve = Just display its a negative number
# + ve  = Check number is even or odd

# Take input from user
data = input("Please enter your number : - ")
data = int(data)

# Approach -1
if(data < 0 ):
    print("This is Negative Number")
else:
    if(data % 2 ==0 ):
        print("This is Even Number")
    else:
        print("This is Odd Number")

# Approach -2
if( data>= 0 ):
    if(data % 2 ==0 ):
        print("This is Even Number")
    else:
        print("This is Odd Number")
else:
    print("This is Negative number")