'''
marks = int(input("Hi Student Enter your marks:: "))

if marks>=90:
    print("You got A Grade, Congrats")
elif (marks>=80) & (marks < 90):
    print("You got B Grade, Congrats")
elif (marks>=70) & (marks<80):
    print("You got C Grade, Congrats")
else:
    print("You got D grade, Congrats")

'''

# check if number is odd or even
'''
n = int(input("Enter any natural number :: "))

if n>0:
    if n%2 == 0:
        print("number is even")
    else:
        print("odd")
else:
    print("kindly add natural numbers only")
    
'''

# Check if numnber is multiple of 7 or not
n = int(input("Enter any number to check if it is multiple of 7 :: "))

if n%7 == 0:
    print("Yes")
else:
    print("No")
