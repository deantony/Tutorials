#Strings are words
x = "This is a string"
#Numbers can be

#integers (int) which are whole numbers
x = 1
#floats which have decimals
x = 1.5


#lists are groups
x = ["List can have strings", 1, 1.5, "Numbers or other lists", [1, 2, 3]]
print(f"The whole list {x}")
#to data in lists use brackets. The index, which is the spot inside the list, starts with 0
print(f"The first item in the list (index = 0) x[0] = {x[0]}")
#Since the last item in the list is a list, you would have to identify the index of that list as well. otherwise you would still have a list
print(f"Not providing an index for the second list x[4] = {x[4]}") #Did not identify which item in the second list
print(f"providing the index for the second list, x[4][0] = {x[4][0]}") #Accessing the first item (index = 0) in the second list

#you can also get the last item by using -1 as the index
print(f"x[-1] = {x[-1]}")
print(f"x[-1][0] = {x[-1][0]}")
