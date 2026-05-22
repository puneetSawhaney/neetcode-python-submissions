# dictionary in python

dict = {"1" : "A", "2": "B", "3": "C"}
print(dict, type(dict))

# output 
# {'1': 'A', '2': 'B', '3': 'C'} <class 'dict'>

# in dictionary we can store lists and tuples as well

dict = {"1" : "A", "2": "B", "3": "C", "4": [1,3,4,5]}
print(dict, type(dict))
# output
# {'1': 'A', '2': 'B', '3': 'C', '4': [1, 3, 4, 5]} <class 'dict'>

# key should be tuple only as key should never change, floating and integers also we can make keys
# Dictionary is mutable, unordered & don't allow any duplicate keys

print(dict["1"])
# output => A
# if I don't give quotes here then it will give error as there in key 1 in dictionary

# empty dict

nDict = {}

nDict[1] = "ABC"

print(nDict)
# output
# {1: 'ABC'}


# nested Dictionaries
# any keys value can be another dictinoary

student = {
    "name" : "Puneet",
    "marks" : {
        "maths": 80,
        "science": 98
    }
    
}

print(student["marks"])
# output
# {'maths': 80, 'science': 98}

# methods in Dictonary

# student.keys(), gives all the keys of the dictionary
# we can also typecase these keys into list
# len(students), give length of dictionary

# student.values(), gives collection of all the vaues
# student.items(), gives all key values pairs as tuple
# student.get("key"), returns key according to value
# student.update(anykey), insert specific items in dictionary
student.update({"city": "delhi"})
print(student)

# output
# {'name': 'Puneet', 'marks': {'maths': 80, 'science': 98}, 'city': 'delhi'}

# if we add older key in new update so then new value will get updated on older value of already existing key



###################
#Sets
########################

# collection of unordered items
# each element in sets will be unique and sets are immutable

# can't store list and dictionary inside set as these two are mutables

# these also contains all elements inside {}

set1 = {1,2,3,5, "hello"}

# if we try to set duplicates values, these duplicates gets ingnored only 1st occurence will be considered

print(len(set1))
# output => 5


# empty set cant be similar to empty dictionary
# empty set
set2= set()

# above is empty set


# methods with Sets

set2.add(1) # 1 will get added  to set2

# sets are mutable but elements inside sets are immutable

set2.add(20)
set2.add(2)

set2.remove(20)

print(set2)
# output => {1, 2}
# add tuple
set2.add((2,4,6))
print(set2)
# output => {1, 2, (2, 4, 6)}

# adding list
#set2.add(["addinglist", " "])
print(set2)
# output
'''

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 114, in <module>
TypeError: unhashable type: 'list'
'''

# to clear all the elements of set
# set2.clear(), it will clear

set2.pop() # removes random val;ue
print(set2)

# output
# {2, (2, 4, 6)}
# removed 1st element


# set.union(set2), unique values from both sets and returns new set
# set.intersection(set2), common values from both sets and returns new set

print(set1.union(set2))
# output => {1, 2, 3, (2, 4, 6), 5, 'hello'}

print(set1.intersection(set2))
# output => {2}


### 
# practice questions
###

# store following word meaning in dictionary

dic = {
    "table" : "a piece of furniture",
    "cat": "a small animal"
    }

print(dic)
# output
# {'table': 'a piece of furniture', 'cat': 'a small animal'}

###
# you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students

# we will use set here 
set1 = {"python", "java", "C++", "python", "javascript"}
set2 = { "java", "python", "C++", "C"}
print(set1)
print(set2)
set3 = set1.union(set2)
print(set3)
# output
# {'javascript', 'C', 'java', 'C++', 'python'}

print(len(set3))
#5
# output


####
# figure out a way to store 9 & 9.0 as separate values in set

set4 = set()

set4.add(("int",9))
set4.add(("float",9.0))

print(set4)
#############{('float', 9.0), ('int', 9)}

