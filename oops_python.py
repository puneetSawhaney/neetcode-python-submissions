# oops with python

# to decrease redundancy and increase reusability

# how to create objects
# instance = object both are same thing

class Student:
    name="puneet"
    
    
s1 = Student()
print(s1, type(s1))

# output => <__main__.Student object at 0x7fc353565c40> <class '__main__.Student'>

# we can print name as well
print(s1.name, type(s1.name))
# output => puneet <class 'str'>


# constructor in class
# __init__()
# this function always gets executed, whenever object is being intiated
# in above class __init__ function is not here, so python by itself creates that and uses that function

class Student:
    college = "Abc College"
    def __init__(self, name, marks ):  # 
        # 1st paraneter is always self which is reference object created, that can be s1 or anything, this constructor gets invoked by itself
    
        # s1 is self only if I will create s2 that is again self for that refernce
        print("new student")
        self.name = name  # attributes
        self.marks = marks
    
    
s1 = Student("Puneet", 89)  # here we are passing name to class Student and it gets passed to init constructor
s2 = Student("Aman", 88)
print(s1, type(s1))


# we can print name as well
print(s1.name, s1.marks, type(s1.name))
print(s2.name,s2.marks, type(s2.name))
'''
new student
<__main__.Student object at 0x7a2f0aa79cd0> <class '__main__.Student'>
Puneet <class 'str'>
Aman <class 'str'>


Puneet 89 <class 'str'>
Aman 88 <class 'str'>

'''


## __init__ is default constructor
## parameterized contructors are those that accept parameters



# Class & instance attributes


# instance attairbutes => different for each object

# each student (class) => all the student name will be different

# any data that is different for every object then we use self. before attributes

# class attributes => different for each class
# if all students from same college then we can college will be same, then there will be one common attribute for all the students, as creating separate attribute for same data is not memory efficient, then we make such data as class attributes
# can be accessed by using Student.college but for accessing object attribute or instance attributes then we need to create object


## # if we have same class attribute and same object attribute then precedence / priority is given to object attribute


###########################
# METHODS
##############################

# class can have attributes => properties , what we can do
# class can have methods => functionalities of that class that belong to objects

# functions written inside class are methods

class Student:
    college = "Abc College"
    def __init__(self, name ):  # 
        # 1st paraneter is always self which is reference object created, that can be s1 or anything, this constructor gets invoked by itself
    
        # s1 is self only if I will create s2 that is again self for that refernce
        print("new student")
        self.name = name  # attributes
        
    def welcome_Student(self):   # self is mandatory
        print(" Hi", self.name  , " welcome to our college")

st = Student("Puneet")
st.welcome_Student()

# outout ==>  Hi Puneet  welcome to our college





## practice

# create student class that takes name & marks of 3 subjects as arguments in constructor, then create method to print average



class StudentInfo():
    def __init__ (self, name, marks):
        self.name= name
        self.marks = marks
    def avgMarks(self):
        avg =0
        totalmarks= 0
        for markEach in self.marks:
            totalmarks += markEach
            
        avg = totalmarks/len(self.marks)
        
        return avg
        
####
# we cam write avg method similar to below code as well
'''
def avgMarks(self):
    return sum(self.marks) / len(self.marks)

'''



###

diction = {"Aman": (40,60,90), "Puneet": (55, 88, 98)}

for pair in diction.items():
    print(pair[0], " ", pair[1] )
    
    obj = StudentInfo(pair[0], pair[1])
    print("Average of " , pair[0], " is ", obj.avgMarks())
    
    
    
    # output
    
    
    '''
    
Aman   (40, 60, 90)
Average of  Aman  is  63.333333333333336
Puneet   (55, 88, 98)
Average of  Puneet  is  80.33333333333333
'''

##### decorator we use to specify that we are creating static method
'''
@staticmethod   # decorator
def college():
    print("ABC College")

# decorator changes the behavior of the normal funciton
# here self is not important that's why we can create static methods at class level
'''
