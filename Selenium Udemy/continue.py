#continue skips the remaining part of the loop here is an example to not print the result when the result is divisible by 10

number = input("Enter a number")

for i in range(1,11):
    if((int(number)*i) %10==0):
        continue
    print(int(number)*i)