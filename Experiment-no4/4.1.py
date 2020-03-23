# Write a python program to implement different file handling operations.

# Good to implement File program with try-catch 
# 1. Opening a file.
try:
    file = open('Experiment-no4/test.txt') 
    for i in file:
        print(file.read())
# You can use IOException also
except Exception as e:
    print('Something went wrong \n', e)
finally:
    file.close()

print('------------/------------')

# 2. Reading a file.
f = open('Experiment-no4/read.txt', 'r')
print(f.read())

print('------------/------------')

# 3. Write a file.
f = open('Experiment-no4/write.txt', 'a')
f.write('Hello this file is created using file handling using python.\n')
# Appending file(Just add 'a', instead of 'w')
f.write('This line is appended to write.txt file')
