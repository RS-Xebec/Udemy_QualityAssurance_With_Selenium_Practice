# Take a marks from user and check, if number is > 100 or < 0, this is invalid marks
# if number is in between 0 -100 then display valid marks

# Conditional OR

marks = input("Please enter your subject marks : - ")
marks = int(marks)

# Check condition for > 100 or < 0
if(marks > 100 or marks < 0):
    print("It's Invalid Marks")
else:
    print("Valid Marks")