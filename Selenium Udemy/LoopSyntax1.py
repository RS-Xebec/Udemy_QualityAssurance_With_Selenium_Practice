#For Loop with final Range 
for i in range(10):      #Starting point will always be zero if it is not given
    print(i)


number=input("Enter your number: ")
for i in range(int(number)):
    print(i)


#For Loop with starting and final Range

number=input("Enter your number:")


for i in range(1,11):
    print(number + "*" +  str(i) + "=" + str(int(number)*i))


#For loop with Starting value , final value and increment value
for i in range(1,11,2):
    print(i)


#For loop with Starting value , final value and Decrement value
for i in range(10,0,-1):
    print(i)
for i in range(10,0,-2):
    print(i)

#Task Ask a number from a user and print the reverse table of that number
number=input("Enter your number:")

for i in range(10,0,-1):
    print(number + " * " + str(i) + "= "+ str(int(number)*i))


#Create a list First
list1= [1,3,5,7,9,'Testing','World']

for i in list1:
    print(i)

#List with multiple numeric values and finding the sum
l1=[1,2,3,4,5,6,7,8]
z=0;
for i in l1:
    z=z+i
print("The sum is " + str(z))

