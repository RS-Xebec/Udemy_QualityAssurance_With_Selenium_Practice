#Concatenation of list
programminglanguage=[2025,'Java','C#','Python', True, False]
programminglanguage_latest = ['PHP','Ruby']

final_list= programminglanguage + programminglanguage_latest
print(final_list)
print(len(final_list))

#Write Operations on the list
#Update value on list
programminglanguage[2]="C++"
print("***********Updated List************")
print(programminglanguage)


#Insert values to list It will put the new value to the index and move the existing value to the next index
programminglanguage.insert(2,"PHP Language")
print("***********Added Value in the List************")
print(programminglanguage)


#Delete value from the list
programminglanguage.remove("Java")
print("***********Deleted Value in the List************")
print(programminglanguage)