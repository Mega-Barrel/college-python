# Write a python program to implement Lambda, map, reduce, filter functions.

# 1. Lambda() function.
'''
a. This function can have any number of arguments but only one expression,which is evaluated and returned.
''' 

# This is a function for finding cube root.
def cube(y): 
    return y*y*y; 
  
# Lamda is used to find the cube root.
g = lambda x: x*x*x 
print('Using lambda')
print(g(5)) 

print('+------------/------------+')

print('Using function')
print(cube(5)) # Print statement for the def method. 

print('------------/------------')

# 2. map() function.
'''
map() function returns a map object(which is an iterator) of the
results after applying the given function to each item of a given iterable.
Syntax: map(fun, iter)
Parameters: fun : It is a function to which map passes each element of given iterable.
            iter : It is a iterable which is to be mapped.
'''
# python code to return double of number
def addition(n):
    return n + n

numbers = (1, 10, 12, 5)
result = map(addition, numbers)
print('Using map() function: ', list(result))

# map() function using lambda()

number = (1, 2, 3, 4) 
result = map(lambda x: x * x, number) 
print('Using lambda() inside map() function: ', list(result)) 

print('------------/------------')

# 3. reduce() function.
'''
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
mentioned in the sequence passed along.
This function is defined in “functools” module.
syntax: reduce(fun,seq)
'''
import functools # for using reduce() function.
lis = [1, 3, 5, 7]
print('Using reduce() function; The sum of elements is:', end='')
print(functools.reduce(lambda a,b: a+b, lis)) 

print('------------/------------')

# 4. filter() function.
'''
The filter() method filters the given sequence with the help
of a function that tests each element in the sequence to be true or not.
Syntax: filter(function, sequence)
Parameters: function: function that tests if each element of a sequence true or not.
            sequence: sequence which needs to be filtered, it canbe sets, lists, tuples, or containers of any iterators.
Returns: returns an iterator that is already filtered.
'''
sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# For odd number
result = filter(lambda x: x % 2, sequence)
print('Using filter() function for odd number:', list(result))
# For even number
result = filter(lambda x: x % 2 == 0, sequence)
print('Using filter() function for even number:', list(result))
