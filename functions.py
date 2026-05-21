# understanding functions in python

##############################################

# 1. built in functions
# int(), float(), min(), max(), len()
# 2. modules\
# python libraries contains functions can be used in our own code 
# like, math, random, string

# math module

import math
print(dir(math))
# gives all math functions
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print(math.pi)
# 3.141592653589793

# if we don't want full name of these modules we can use alias 'as'
# import math as m, now i will not use math everytime, i will use m instead

# if I want specific function to be imported instead of all functions from one module

from math import sin, cos, pi
# here we can't use math that will give error we can directly use sin, cos, pi

print(cos(30))

print(pi)
print(sin(90))
#print(tan(20))  # gives error as it is not imported

'''

0.15425144988758405
3.141592653589793
0.8939966636005579
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 33, in <module>
NameError: name 'tan' is not defined

'''




# 3. user defined
# created by user only
def greet():
    print("Hi How are you doing")
    
# Now we will call this function
greet()
# output
# Hi How are you doing

# function never gets executed till it gets called. Interpretation gets line by line but print happens only when we will call that function

# function with parameters

# function will take list of names and greets everyone in the list

# 3. write the function
def greeteveryone(l):
    for each in l:
        print("Hi", each)
    
    
# 1. create list with names

l = ["Aman", "Riya", "Ankita"]

# 2. call the function
greeteveryone(l)

'''
Hi Aman
Hi Riya
Hi Ankita
'''

