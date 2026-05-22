# functions & recursion

# we use funcitons to reduce redundancy
# to avoid repetition of same piece of code

#####
# Function
########

def sum(a,b):
    s = a+b
    return s
    
print(sum(2,5))
# output  => 7
## 
print(sum(12,5))
# output => 17
#####################


# Recursion
# when a function calls itself repeatedly
def show(n):
    if n==0:
        return
    print(n, end=", ")
    return show(n-1)


show(5)
# output => 5, 4, 3, 2, 1, 

## factorial using recursion
print()
def fact(n):
    if (n==1 or n==0):
        return 1
    return n * fact(n-1)


print(fact(5))
# output => 120


####
# recursive function to calculate sum of first n natural numbers

def cal_sum(n):
    if n == 0:
        return 0
    return n + cal_sum(n-1)



print(cal_sum(10))
# output 55

# recursive function to print all elements in alist

def print_list(li, idx):
    if idx == len(li):
        return
    print(li[idx], end = " , ")
    return print_list(li, idx+1)
    
    



li = [1, 2,4,6,77, "ab", "78", 9.0]

print_list(li, 0)
# output => 1 , 2 , 4 , 6 , 77 , ab , 78 , 9.0 , 
