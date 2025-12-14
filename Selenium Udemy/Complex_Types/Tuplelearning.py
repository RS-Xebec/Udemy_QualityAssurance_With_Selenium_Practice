#dEFINE A TUPLE
programminglanguage = (2021,"C#","Java","Python",True, False)

#Display all values of Tuple by giving index
print(programminglanguage[3])
print(programminglanguage[2:5])
print(programminglanguage[2:])
print(programminglanguage[:5])


#Find length of the tuple
print(len(programminglanguage))
tuple_length=(len(programminglanguage))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "apple")
print(thistuple[-4:-1])
print(thistuple.count("apple"))   #count Returns the number of times a specified value occurs in a tuple
print(thistuple.index("banana"))