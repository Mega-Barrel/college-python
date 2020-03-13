# Write a program to implement inheritance and polimorphism with method overloading and method overwriding.

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
    def add(self,x,y):
        self.x = x
        self.y = y
        print(x+y)
    def add(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print(x+y+z)
m = MO()
m.add(23,23,11)
m.add(32,22)