# Dictionary & Sets

# Sets are also used as data structure only
# all elements in set are unique
# we use curly braces to create sets, [] for list () for tuples

a = {1,2,2,3,5,66,7,7,9}
print(a)
# Output => {1, 66, 3, 2, 5, 7, 9}
# only unique elements if you see

for element in a:
    print(element*2, end = " ")
    
# output => 2 132 6 4 10 14 18 

# here in sets we can't access elements using index
# list, tuple & sets only store values where as Dictionary store key value pairs like maps in other programming languages

###########################################
# Dictionary
###########################################

# key can be of any type


# 1. Empty Dict
my_dict= {}
print(my_dict, type(my_dict))
# output  = > {} <class 'dict'> 
# 2. Dictionary with same kind of key value pairs

my_dict= {1: 'ab', 2: 'cd', 3:'de'}
print(my_dict, type(my_dict))
# output  = > {1: 'ab', 2: 'cd', 3: 'de'} <class 'dict'> 

# 3. Dictionary with different kind of key value pairs
my_dict= {'random': 'ab', 2: 'cd', 3:['de', 2,8.7]}
print(my_dict, type(my_dict))
# output  = > {'random': 'ab', 2: 'cd', 3: ['de', 2, 8.7]} <class 'dict'> 

# 4. 


marks= {'a': 34, 'vf': 56, 'gh':24, 'av':223}

print(marks['vf'])
# output => 56

# iterating over dictionary
sq = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}

for i in sq:
    print(sq[i], end=", ")
    
# output => 1, 4, 9, 16, 25, 36, 

print()

# we can update any key value pairs, also we can merge dictionaries

# if key is already present, value gets updated takes latest one

