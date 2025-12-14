#break statement stops the loop if the condition is true
number=input("Enter Your Number ")

for i in range(1,11):
    if(int(number)*i==60):
        break
    print(int(number)*i)