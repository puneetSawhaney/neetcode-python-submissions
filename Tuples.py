# Tuples in python
# immutable unlike lists we can't change elements here in tuple, but these are memory efficient and do not have performance overhead
# strings are also immutable, we need to convert that to list using list(stringVariablename)
# how to declare tuples

# 1. empty
my_tuple = ()
print(my_tuple, type(my_tuple))

# 2. same type of elements
my_tuple = (1, 2, 3)
print(my_tuple, type(my_tuple))

# 3. mixed elements
my_tuple = (1, "as", 134.34)
print(my_tuple, type(my_tuple))

# Output of all above declarations and print

'''
() <class 'tuple'>
(1, 2, 3) <class 'tuple'>
(1, 'as', 134.34) <class 'tuple'>

'''

