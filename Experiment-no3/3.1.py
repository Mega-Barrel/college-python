# Write a program to implement Class, Object, Static method and inner class.

# 1. class:
class empty:
    pass

print('------------/------------')

# 2. Object:
class student:
    print('Hello World!')
a = student()

print('------------/------------')

# 3. static method:
'''static method is bound to a class rather than the objects for that class. 
This means that a static method can be called without an object for that class.
'''
class Calculator:
    @staticmethod
    def multiplyNums(x, y):
        return x * y
print('Product:', Calculator.multiplyNums(15, 2))

print('------------/------------')

# 4. inner class:
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        # Always create object of innerclass in main class.
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.rollno)
        # Calling laptop show method
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "dell"
            self.cpu = 'i3'
            self.ram = 8

        def show(self):
            print('Laptop configuration: ')
            print(self.brand, self.cpu, self.ram, 'GB')

s1 = Student('Saurabh', 2)
s1.show()
lap1 = Student.Laptop()


