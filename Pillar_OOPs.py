
######################################################
'''
Pillars in OOPs

A Abstraction
P Polymorphism
I Inheritance
E Encapsulation

'''
##############################################################


############################################
# Abstraction
# hiding the implementation details of a class and only showing the essential features to the user


class Car:
    
    def __init__(self):
        self.accelerator = False   # coomon property of car
        self.brk = False
        self.clutch = False
        
    def start(self):
        
        self.clutch = True
        self.accelerator = True
        print("Car started")

car1 = Car()
car1.start()


# output => Car started

# when we created object, user doesnot know what is happening in the background, as soon as he started the car, the car got started, right that is abstraction only

# Encapsulation
# wrapping data and functions into a single unit(object)

# till now whatever we have worked in oops, is encapsulation only 
# like we created classes and wrapped everything inside classes


########################



### 
# practice
# create account class with 2 attribute - balance & account no.
# create methods for debit, credit & printing the balance

class Account():
    balance = 50000
    def __init__(self, bal, acc):
        self.balance = bal
        self.accNo = acc
        
    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            
            print("Amount debited :: ", amount)
            print("FInal Balance :: ", self.balance)
        
        
    def credit(self, amount):
        if amount>0:
            self.balance += amount
            
            print("Amount credited :: ", amount)
            print("FInal Balance :: ", self.balance)
            
        
    
    def print_Bal(self):
        
        print("Your Balance :: ",self.balance)
        
        
        
        
acc1 = Account(25000, 4636)
acc1.print_Bal()
acc1.debit(10000)
acc1.credit(70000)



'''
Amount debited ::  10000
FInal Balance ::  15000
Amount credited ::  70000
FInal Balance ::  85000



'''
    
