# Write a python program to implement Lambda, map, reduce, filter functions.

# 1. Lambda program.
# a. This function can have any number of arguments but only one expression,
#    which is evaluated and returned.
# b. 

# This is a function for finding cube root.
def cube(y): 
    return y*y*y; 
  
# Lamda is used to find the cube root.
g = lambda x: x*x*x 
print('Using lambda')
print(g(5)) 

print('------------/------------')

print('Using function')
print(cube(5)) # Print statement for the def method. 