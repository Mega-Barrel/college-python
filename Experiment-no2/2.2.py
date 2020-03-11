# Write a program to implement for loops.

# 1. For loop:
print("List Iteration:") 
l = ["Hello", "World", "!"] 
for i in l: 
    print(i) 

print('------------/------------')

# 2. Nested for loop:
for i in range(1, 5): 
    for j in range(i): 
         print(i, end=' ') 
    print() 

print('------------/------------')

# 3. For loop with else statement:
for x in range(6):
    print(x)
else:
    print("Finally Finished")