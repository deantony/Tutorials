list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected_number = 5



for i in range(len(list)): #loop through each i in the range of 0 to the list length
    if list[i] == selected_number: # i is set to be the index of list
        print(i) #print the index "selected_number" is at 

#basically this program does:
"""
if list[0] == 5:
    print(0)
if list[1] == 5:
    print(1)
if list[2] == 5:
    print(2)
"""
#and so on...until it gets to the end of the list
