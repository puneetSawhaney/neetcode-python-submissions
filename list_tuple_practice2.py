# lists in python
# practice and brush up
# similar to arrays to store some elements
# list properties are similar to strings when we want to access indexes
# lists are mutable, access and updating is possible
# strings, tuples are immutable, we can access but we can't update

# slicing is possible here with lists as well
# list_name[start_index: endindex] gives sublist

# functions with list
# list.append(4) , 4 needs to be appended
# list.sort() , by default ascending order
# list.sort(reverse=True), for descending order
# list.reverse(), reverses the list
# list.insert(index, element_TobeInserted) , 1st argument the index where 2nd argument needs to be inserted

# list.remove(1), removes 1st occurence of that element
# list.pop(3) , pops the element from index 3 from list

# list.copy(), creates the copy 

# similarly there are so many ,methods



# Tuples in Python

# immutable, memory efficient and give good performance

# once tuple is created we can't change the elements, we can't insert, we can't remove

# lists are stored in []
# tuples are stored in ()
# Sets stored in {}
# Dictionary also stored in {}

# if only single value is there to be created as tuple still ad , after that value
# tup = (1, )
# else the interpreter takes it as whatever datatype it is at runtime and not tuple

# Slicing works here as well

# Methods

# tup.index(ele), this returns index
# tup.count(3), counts occurences of 3 in tuples



# Practice

# Get 3 names from user and store it in list
'''
n1 = input("Enter 1st name :: ")
n2 = input("Enter 2nd name :: ")
n3 = input("Enter 3rd name :: ")

lis = [n1, n2, n3]


print("Your list :: ", lis)
'''

# Check if list contains a palindrome of elements

# 1. reverse 
# 2. compare

def palindrome(list1):
    revlist = []
    # reverse
    for ele in list1:
        revlist.append(ele)
    
    print(revlist)
    
    if revlist == list1:
        return True
    else:
        return False


l1 = [1,2,3,2,1]
l2 = [1, "abc", "abc", 1]

print(palindrome(l1))
print(palindrome(l2))

# output => True
# output => True

##################
# tuples practice
#################

# count number of students with the A grade in the tuple
tup = ("C", "D", "A", "F", "h","i","D", "A")
print(tup.count("A"))

# output => 2

# Store the above values in a list & sort them from "A" to "D"

lis= list(tup)
print(lis.sort()) # prints None

print(lis)
# output => ['A', 'A', 'C', 'D', 'D', 'F', 'h', 'i']
