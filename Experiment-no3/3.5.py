# Write a program to implement constructor in python.

# 1. Default constructor.
class DemoClass:
    num = 101

    # Creating a method
    def read_number(self):
        print(self.num)

# creating object of the class
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()

print('------------/------------')

# 2. Parameterized constructor.
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
# Creating object for the class
std1 = student('Saurabh', 18)

#calling the instance method using object
print(std1.name, ':', std1.age)
    
