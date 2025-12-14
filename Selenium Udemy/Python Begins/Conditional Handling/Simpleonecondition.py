#Take input from user - number
#Check if this number is Even, Print this is even number
#Don't do anything if number is odd 

data = input("Please Enter your number: ")
data = int(data)

if(data     %2) == 0:
    print("This is even number")
    print("Ths is my second line")
    print("This is end of condition")
print("This is Print Statement ouside of the condition")