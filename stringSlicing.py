
# About Strings
# index starts from 0 nto len(n-1)
# negative index -1 means last character similar for all the other elements

fruit = "Apple"

print(fruit[-2])

# Output => l because 2 was -1 and l is -2


# Slicing with Strings, for accessing range of characters
st = "something is here" 
# spaces are also character

print(st[1:4]) 
# 1 start index , 4 index -1 
# output from index 1 to index 4
# ome

print(st[:4])
# output will be till 4 index from first index by default

print(st[7:])
# output will be from 7 index till last index by default

print(st[0:8:2])
# 3rd argymnet is step like how many elements needs to be skipped


# output for all 3 
'''
some
ng is here
smti
'''

print(st[::-1])

# it starts from last
# ereh si gnihtemos
# this is reverse of any string

print(st[0:5:-1])

# nothing gets printed for above
# why => direction matters alot, here we are going toward left to right but direction is -1 means opposite direction so that's why nothing got printed

print(st[-1:4:-1])

#output :: ereh si gnih
# here it will start from last element till 4th element skipping -1 part as we are going in same direction
# 4 th index is not include
