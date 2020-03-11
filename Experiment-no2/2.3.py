# Write a program to implement function.

# 1. Normal function:
def myfunction():
    print('This statement is called using a function.')
myfunction()

print('------------/------------')

# 2. Parameterized function:
def fact(x):
    if x == 1:
        return 1
    else:
        x = x * fact(x - 1)
    return x
print(fact(5))

