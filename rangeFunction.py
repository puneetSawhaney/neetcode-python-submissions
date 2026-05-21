# Range function implementation

a= range(10)

print(a)
# output => range(0, 10)

# this function doesnot create any numbers in memory it just keep the record of range from 0 to n-1

a= list(range(10))

print(a)

# output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# so here list created its place in memory and stored all numbers in range from 0 to n-1

# Rannge can take up to 3 arguments
# if one argument, then it takes end point
# if two argument, 1st is start and last is end
# if three argumnet, 1st is start , 2nd is end, 3rd is incremental number means

# range(3, 11, 2) => 3, 5, 7, 9
# generates with 2 increment with each number


# we use range widely in loops

# for and while loop in python

# for loop

for x in range(10):
    print(2*x)
    
    
# output
'''
0
2
4
6
8
10
12
14
16
18
'''

for x in range(0, 10, 4):
    print(2*x, end = " ")
# output as it skipped 5 elements each time   
'''
0 8 16
'''
print()
# for loop for list

listSome = ['abc', 'def', 'ghi']

for name in listSome:
    print(name, end= ", ")
 
 # output
 # abc, def, ghi, 
