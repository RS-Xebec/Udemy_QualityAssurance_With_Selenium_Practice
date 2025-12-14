# Take 1 number from User
# Check if number is +ve and multiple of 2 , then print even number
# Check if number is +ve and not multiple of 2 , then print odd number

# Taking input
num = input("Please enter your number: - ")
num = int(num)

if((num >= 0) and (num%2==0)):
    print("This is Positive Even number")
elif((num>=0) and (num%2!=0)):
    print("This is Positive Odd number")


