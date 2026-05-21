# Lists in python

mylist = []
# can be empty
print(mylist, type(mylist))
mylist = [1,2,3,]
print(mylist, type(mylist))
# can contain numbers

mylist = [1, "anbc", 2.3]
# can contain different type of elements

print(mylist, type(mylist))

# output of above 3 statements
'''
[] <class 'list'>
[1, 2, 3] <class 'list'>
[1, 'anbc', 2.3] <class 'list'>
'''

# how to access anything in list

num =[1,2,4,56,7,8]
print(num[3])
# output => 56, at 3 index we have 56

# again negative indexing is there 
# -1 = 8, -2 = 7 likewise
# all the sequences contains negative indexing whether it be strings, list or any 

print(num[2:5])

print(num[-1:3:-1])

# output
'''
[4, 56, 7]
[8, 7]
'''

# we can update/ delete elements from list, as it is mutable
# update element
num[1] = 76
print(num)
# output = [1, 76, 4, 56, 7, 8]

# delete element

del num[1]
print(num)

# output = [1, 4, 56, 7, 8]
'''
76 that we inserted earlier is not here we can delete the complete list in similar way 
"del num"
'''
########################################
#list Comprehension
########################################

# new_list =[expression for item in list if condition]
pow2 = [i for i in range(10)]
print(pow2)

# list got created
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for adding confition, lets say for even numbers
pow2 = [i for i in range(10) if i%2 == 0]
print(pow2)
# output => [0, 2, 4, 6, 8]

power = [ 2**i for i in range(10)]
print(power)
# output == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

#############################################
# List Methods
##############################################

# append

newList = [1,2,3]
print(newList)
# [1, 2, 3]

newList.append(4)  # adds in last of list
print(newList)

# [1, 2, 3, 4]

##############################################
# Indertion at some index in list
#############################################


newList.insert(1, 2.3)

print(newList)
# output => [1, 2.3, 2, 3, 4]

# elements from index 1 pushed further as we  inserted element at index 1, there is none of the elements got removed


########################################
# Sorting
######################################

list1 = [7,346,7,4,22325,35,68,123]
print("Before Sorting :: ", list1)
'''
Before Sorting ::  [7, 346, 7, 4, 22325, 35, 68, 123]
'''
list1.sort()
print("After Sorting :: ", list1)

# Output
'''

After Sorting ::  [4, 7, 7, 35, 68, 123, 346, 22325]
'''

# By default it is ascending order, if we add reverse= True it then does descending order

list1.sort(reverse=True)
print("After Sorting  with reverse True:: ", list1)
# output
# After Sorting  with reverse True::  [22325, 346, 123, 68, 35, 7, 7, 4]

list1.reverse()
print(list1)
# output => [4, 7, 7, 35, 68, 123, 346, 22325] 


list1.clear()



print(list1)
# Output list will be there but elements got clear
# []

###############################################
# Functions of List
############################################

list1 = [7,346,7,4,22325,35,68,123]
print("Len :: ",len(list1))
print("max :: ",max(list1))
print("min :: ",min(list1))
print("sum :: ",sum(list1))
# Output
'''
Len ::  8
max ::  22325
min ::  4
sum ::  22915
'''
# convert any sequence of characters to list

seq = "Aman"
print(list(seq))
# Output 
# ['A', 'm', 'a', 'n']
