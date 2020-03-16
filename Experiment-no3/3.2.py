# Write a program to implement inheritance and polimorphism with method overloading and method overriding.

# 1. inheritance:
class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def printname(self):
        print("Name is", self.name)
        print("Age is", self.age)
        print("Graduation year is", self.graduationyear)     
    # Creating a child class which inherits properties of parent class.
class Student(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.graduationyear = year

p1 = Student("Saurabh", 18, 2022)
p1.printname()

print('------------/------------')


# 2. polimorphism:
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
    def language(self): 
        print("Hindi the primary language of India.")   
    def type(self): 
        print("India is a developing country.") 
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
    def language(self): 
        print("English is the primary language of USA.") 
    def type(self): 
        print("USA is a developed country.") 
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 

print('------------/------------')


# 3. method overloading:
class MO:
    def add(self, a = None, b = None, c = None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s
m = MO()
print('Addition is:' ,m.add(1,2,2))
print('Addition is:' ,m.add(1,2))

print('------------/------------')


# 4. method overriding:
class A:
    def show(self):
        print('In A')

class B:
    def show(self):
        print('In B')

a1 = B()
a1.show()